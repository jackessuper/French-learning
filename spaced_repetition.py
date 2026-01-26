"""
Spaced Repetition System (SM-2 Algorithm)
==========================================
Implements the SuperMemo SM-2 algorithm for optimal learning intervals.
Supports multiple users with separate progress tracking.

Quality ratings:
    0 - Complete blackout, no recall
    1 - Incorrect, but remembered upon seeing answer
    2 - Incorrect, but answer seemed easy to recall
    3 - Correct, but with significant difficulty
    4 - Correct, with some hesitation
    5 - Perfect response, instant recall
"""

from datetime import datetime, timedelta
from database import get_connection
from users import get_or_create_user


def calculate_sm2(quality: int, repetitions: int, ease_factor: float, interval: int):
    """
    Calculate new SM-2 values based on review quality.

    Args:
        quality: Rating 0-5 (0=blackout, 5=perfect)
        repetitions: Number of successful reviews in a row
        ease_factor: Current ease factor (minimum 1.3)
        interval: Current interval in days

    Returns:
        tuple: (new_repetitions, new_ease_factor, new_interval)
    """
    quality = max(0, min(5, quality))

    if quality < 3:
        new_repetitions = 0
        new_interval = 1
        new_ease_factor = ease_factor
    else:
        new_repetitions = repetitions + 1
        new_ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        new_ease_factor = max(1.3, new_ease_factor)

        if new_repetitions == 1:
            new_interval = 1
        elif new_repetitions == 2:
            new_interval = 6
        else:
            new_interval = round(interval * new_ease_factor)

    return new_repetitions, new_ease_factor, new_interval


def review_card(user: str, card_id: int, quality: int):
    """
    Process a card review and update spaced repetition data.

    Args:
        user: User name
        card_id: The card being reviewed
        quality: Rating 0-5

    Returns:
        dict: Updated progress data including next review date
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    # Get current progress
    cursor.execute("""
        SELECT ease_factor, interval, repetitions
        FROM progress WHERE user_id = ? AND card_id = ?
    """, (user_id, card_id))
    row = cursor.fetchone()

    if row:
        ease_factor = row['ease_factor']
        interval = row['interval']
        repetitions = row['repetitions']
    else:
        ease_factor = 2.5
        interval = 0
        repetitions = 0

    # Calculate new values
    new_reps, new_ease, new_interval = calculate_sm2(
        quality, repetitions, ease_factor, interval
    )

    next_review = datetime.now().date() + timedelta(days=new_interval)

    # Update or insert progress
    cursor.execute("""
        INSERT INTO progress (user_id, card_id, ease_factor, interval, repetitions, next_review, last_reviewed)
        VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(user_id, card_id) DO UPDATE SET
            ease_factor = excluded.ease_factor,
            interval = excluded.interval,
            repetitions = excluded.repetitions,
            next_review = excluded.next_review,
            last_reviewed = excluded.last_reviewed
    """, (user_id, card_id, new_ease, new_interval, new_reps, next_review))

    # Record in history
    cursor.execute("""
        INSERT INTO review_history (user_id, card_id, quality)
        VALUES (?, ?, ?)
    """, (user_id, card_id, quality))

    conn.commit()
    conn.close()

    return {
        'user': user,
        'card_id': card_id,
        'quality': quality,
        'ease_factor': new_ease,
        'interval': new_interval,
        'repetitions': new_reps,
        'next_review': next_review.isoformat()
    }


def get_unlocked_priority(user: str, category: str = None):
    """
    Determine which priority levels are unlocked for a user.

    A priority level unlocks when:
    - At least 80% of cards at previous levels have been reviewed
    - Average ease factor at previous levels is >= 2.3

    Args:
        user: User name
        category: Optional category filter (unlocking is per-category)

    Returns:
        int: Highest unlocked priority level
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("SELECT DISTINCT priority FROM cards WHERE category = ? ORDER BY priority", (category,))
    else:
        cursor.execute("SELECT DISTINCT priority FROM cards ORDER BY priority")

    priorities = [row['priority'] for row in cursor.fetchall()]

    if not priorities:
        conn.close()
        return 1

    unlocked = priorities[0]

    for priority in priorities:
        if category:
            cursor.execute("""
                SELECT
                    COUNT(c.id) as total,
                    COUNT(CASE WHEN p.repetitions >= 1 THEN 1 END) as reviewed,
                    AVG(CASE WHEN p.ease_factor IS NOT NULL THEN p.ease_factor END) as avg_ease
                FROM cards c
                LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
                WHERE c.priority = ? AND c.category = ?
            """, (user_id, priority, category))
        else:
            cursor.execute("""
                SELECT
                    COUNT(c.id) as total,
                    COUNT(CASE WHEN p.repetitions >= 1 THEN 1 END) as reviewed,
                    AVG(CASE WHEN p.ease_factor IS NOT NULL THEN p.ease_factor END) as avg_ease
                FROM cards c
                LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
                WHERE c.priority = ?
            """, (user_id, priority))

        row = cursor.fetchone()
        total = row['total']
        reviewed = row['reviewed'] or 0
        avg_ease = row['avg_ease'] or 2.5

        review_rate = reviewed / total if total > 0 else 0

        if review_rate >= 0.8 and avg_ease >= 2.3:
            unlocked = priority + 1
        else:
            break

    conn.close()
    return unlocked


def get_due_cards(user: str, category: str = None, topic: str = None, limit: int = 20):
    """
    Get cards due for review for a specific user.

    Args:
        user: User name
        category: Optional category filter (e.g., 'general', 'animals')
        topic: Optional topic filter
        limit: Maximum number of cards

    Returns:
        list: Cards due for review, ordered by priority
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().date().isoformat()
    max_priority = get_unlocked_priority(user, category)

    query = """
        SELECT c.*, p.next_review, p.ease_factor, p.interval, p.repetitions
        FROM cards c
        LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
        WHERE (p.next_review IS NULL OR p.next_review <= ?)
        AND c.priority <= ?
    """
    params = [user_id, today, max_priority]

    if category:
        query += " AND c.category = ?"
        params.append(category)

    if topic:
        query += " AND c.topic = ?"
        params.append(topic)

    query += """
        ORDER BY c.category ASC, c.priority ASC, p.next_review IS NULL ASC, p.next_review ASC
        LIMIT ?
    """
    params.append(limit)

    cursor.execute(query, params)
    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return cards


def get_priority_status(user: str, category: str = None):
    """
    Get mastery status for each priority level for a user.

    Args:
        user: User name
        category: Optional category filter

    Returns:
        list: Status of each priority level
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("""
            SELECT
                c.priority,
                COUNT(c.id) as total,
                COUNT(CASE WHEN p.repetitions >= 1 THEN 1 END) as reviewed,
                COUNT(CASE WHEN p.repetitions >= 3 THEN 1 END) as learned,
                AVG(CASE WHEN p.ease_factor IS NOT NULL THEN p.ease_factor END) as avg_ease
            FROM cards c
            LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
            WHERE c.category = ?
            GROUP BY c.priority
            ORDER BY c.priority
        """, (user_id, category))
    else:
        cursor.execute("""
            SELECT
                c.priority,
                COUNT(c.id) as total,
                COUNT(CASE WHEN p.repetitions >= 1 THEN 1 END) as reviewed,
                COUNT(CASE WHEN p.repetitions >= 3 THEN 1 END) as learned,
                AVG(CASE WHEN p.ease_factor IS NOT NULL THEN p.ease_factor END) as avg_ease
            FROM cards c
            LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
            GROUP BY c.priority
            ORDER BY c.priority
        """, (user_id,))

    unlocked = get_unlocked_priority(user, category)

    result = []
    for row in cursor.fetchall():
        total = row['total']
        reviewed = row['reviewed'] or 0
        result.append({
            'priority': row['priority'],
            'total': total,
            'reviewed': reviewed,
            'learned': row['learned'] or 0,
            'avg_ease': round(row['avg_ease'], 2) if row['avg_ease'] else 2.5,
            'review_rate': round(reviewed / total * 100, 1) if total > 0 else 0,
            'unlocked': row['priority'] <= unlocked
        })

    conn.close()
    return result


def get_review_stats(user: str):
    """
    Get overall review statistics for a user.

    Args:
        user: User name

    Returns:
        dict: Review statistics
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().date().isoformat()

    cursor.execute("SELECT COUNT(*) as total FROM cards")
    total_cards = cursor.fetchone()['total']

    cursor.execute("""
        SELECT COUNT(*) as learned FROM progress
        WHERE user_id = ? AND repetitions > 0
    """, (user_id,))
    learned = cursor.fetchone()['learned']

    max_priority = get_unlocked_priority(user)
    cursor.execute("""
        SELECT COUNT(*) as due FROM cards c
        LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
        WHERE (p.next_review IS NULL OR p.next_review <= ?)
        AND c.priority <= ?
    """, (user_id, today, max_priority))
    due_today = cursor.fetchone()['due']

    cursor.execute("""
        SELECT COUNT(*) as reviews FROM review_history
        WHERE user_id = ? AND date(reviewed_at) = date('now')
    """, (user_id,))
    reviews_today = cursor.fetchone()['reviews']

    cursor.execute("""
        SELECT AVG(ease_factor) as avg_ease FROM progress
        WHERE user_id = ?
    """, (user_id,))
    avg_ease = cursor.fetchone()['avg_ease'] or 2.5

    conn.close()

    return {
        'total_cards': total_cards,
        'cards_learned': learned,
        'cards_due': due_today,
        'reviews_today': reviews_today,
        'average_ease': round(avg_ease, 2)
    }


def get_card_progress(user: str, card_id: int):
    """Get progress data for a specific card and user."""
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM progress WHERE user_id = ? AND card_id = ?
    """, (user_id, card_id))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None
