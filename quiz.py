"""
Picture Quiz Module for Kids
=============================
A kid-friendly quiz mode where children see a French word and choose from 4 images.
Integrates with the spaced repetition system for tracking progress.
"""

import random
from database import get_connection
from spaced_repetition import review_card, get_due_cards, get_unlocked_priority
from users import get_or_create_user

# Categories that support picture quizzes (have image data)
QUIZ_CATEGORIES = ['animals', 'food_kids', 'colours', 'body']


def get_quiz_categories() -> list:
    """
    Get list of categories that support picture quizzes.

    Returns:
        list: Category names with image support
    """
    return QUIZ_CATEGORIES.copy()


def get_cards_with_images(category: str) -> list:
    """
    Get all cards from a category that have images.

    Args:
        category: The category to get cards from

    Returns:
        list: Cards with non-null image field
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM cards
        WHERE category = ? AND image IS NOT NULL
        ORDER BY priority, id
    """, (category,))

    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return cards


def get_quiz_question(user: str, category: str) -> dict:
    """
    Generate a quiz question for a user in a specific category.

    Selects a due card from the category (or random if none due),
    finds 3 distractors from the same category, and returns the
    question data.

    Args:
        user: User name
        category: Category to quiz from (must be in QUIZ_CATEGORIES)

    Returns:
        dict: {
            'card': The card being quizzed (with french, english, pronunciation),
            'options': List of 4 options [{id, image}, ...] in random order,
            'correct_index': Index of the correct answer (0-3)
        }
        Returns None if not enough cards with images in category
    """
    if category not in QUIZ_CATEGORIES:
        return None

    # Get all cards with images in this category
    all_cards = get_cards_with_images(category)

    if len(all_cards) < 4:
        return None  # Need at least 4 cards for a quiz

    # Try to get a due card first
    due_cards = get_due_cards(user, category=category, limit=50)
    due_cards_with_images = [c for c in due_cards if c.get('image')]

    if due_cards_with_images:
        # Pick a random due card with image
        target_card = random.choice(due_cards_with_images)
    else:
        # No due cards, pick a random card from category
        target_card = random.choice(all_cards)

    # Get 3 distractors (different cards with images)
    distractor_pool = [c for c in all_cards if c['id'] != target_card['id']]
    distractors = random.sample(distractor_pool, min(3, len(distractor_pool)))

    if len(distractors) < 3:
        return None  # Not enough distractors

    # Create options list with correct answer and distractors
    options = [{'id': target_card['id'], 'image': target_card['image']}]
    for d in distractors:
        options.append({'id': d['id'], 'image': d['image']})

    # Shuffle options
    random.shuffle(options)

    # Find correct index after shuffle
    correct_index = next(i for i, opt in enumerate(options) if opt['id'] == target_card['id'])

    return {
        'card': {
            'id': target_card['id'],
            'french': target_card['french'],
            'english': target_card['english'],
            'pronunciation': target_card.get('pronunciation')
        },
        'options': options,
        'correct_index': correct_index
    }


def answer_quiz(user: str, card_id: int, correct: bool) -> dict:
    """
    Process a quiz answer and update spaced repetition progress.

    Args:
        user: User name
        card_id: The card that was answered
        correct: Whether the answer was correct

    Returns:
        dict: Updated progress info from review_card
    """
    # Map to SM-2 quality ratings:
    # Quiz awards half the progress compared to flashcards:
    # Correct = 3 (correct with difficulty - slower interval growth)
    # Wrong = 1 (incorrect - resets but with minimal credit)
    quality = 3 if correct else 1

    return review_card(user, card_id, quality)


def get_quiz_stats(user: str, category: str = None) -> dict:
    """
    Get quiz statistics for a user.

    Args:
        user: User name
        category: Optional category filter

    Returns:
        dict: Quiz statistics
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    # Base query for cards with images
    if category:
        cursor.execute("""
            SELECT COUNT(*) as total FROM cards
            WHERE category = ? AND image IS NOT NULL
        """, (category,))
    else:
        cursor.execute("""
            SELECT COUNT(*) as total FROM cards
            WHERE category IN (?, ?, ?, ?) AND image IS NOT NULL
        """, tuple(QUIZ_CATEGORIES))

    total_cards = cursor.fetchone()['total']

    # Cards reviewed (have progress)
    if category:
        cursor.execute("""
            SELECT COUNT(*) as reviewed FROM cards c
            JOIN progress p ON c.id = p.card_id AND p.user_id = ?
            WHERE c.category = ? AND c.image IS NOT NULL AND p.repetitions > 0
        """, (user_id, category))
    else:
        cursor.execute("""
            SELECT COUNT(*) as reviewed FROM cards c
            JOIN progress p ON c.id = p.card_id AND p.user_id = ?
            WHERE c.category IN (?, ?, ?, ?) AND c.image IS NOT NULL AND p.repetitions > 0
        """, (user_id,) + tuple(QUIZ_CATEGORIES))

    reviewed = cursor.fetchone()['reviewed']

    # Cards mastered (repetitions >= 3)
    if category:
        cursor.execute("""
            SELECT COUNT(*) as mastered FROM cards c
            JOIN progress p ON c.id = p.card_id AND p.user_id = ?
            WHERE c.category = ? AND c.image IS NOT NULL AND p.repetitions >= 3
        """, (user_id, category))
    else:
        cursor.execute("""
            SELECT COUNT(*) as mastered FROM cards c
            JOIN progress p ON c.id = p.card_id AND p.user_id = ?
            WHERE c.category IN (?, ?, ?, ?) AND c.image IS NOT NULL AND p.repetitions >= 3
        """, (user_id,) + tuple(QUIZ_CATEGORIES))

    mastered = cursor.fetchone()['mastered']

    conn.close()

    return {
        'total_cards': total_cards,
        'reviewed': reviewed,
        'mastered': mastered,
        'progress_percent': round(reviewed / total_cards * 100, 1) if total_cards > 0 else 0
    }


def get_category_info(category: str) -> dict:
    """
    Get information about a quiz category.

    Args:
        category: Category name

    Returns:
        dict: Category info including name, card count, emoji
    """
    category_display = {
        'animals': {'name': 'Animals', 'emoji': '\U0001F43E'},
        'food_kids': {'name': 'Food', 'emoji': '\U0001F34E'},
        'colours': {'name': 'Colours', 'emoji': '\U0001F3A8'},
        'body': {'name': 'Body Parts', 'emoji': '\U0001F9D1'}
    }

    if category not in QUIZ_CATEGORIES:
        return None

    cards = get_cards_with_images(category)

    info = category_display.get(category, {'name': category.title(), 'emoji': '\U0001F4DA'})
    info['category'] = category
    info['card_count'] = len(cards)

    return info
