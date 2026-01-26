"""
Flask Web Application for French Learning
==========================================
A web interface for the French learning system with flashcards,
quiz mode, user management, and progress tracking.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Flask, render_template, request, jsonify, redirect, url_for

from users import get_all_users, get_or_create_user
from vocabulary import get_categories, get_cards
from spaced_repetition import (
    get_due_cards, review_card, get_priority_status,
    get_review_stats, get_unlocked_priority
)
from quiz import get_quiz_categories, get_quiz_question, answer_quiz, get_category_info
from progress import get_summary, get_daily_reviews, get_difficult_cards, get_mastered_cards

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'french-learning-secret-key')

# Category display info
CATEGORY_INFO = {
    'general': {'name': 'General French', 'emoji': '🇫🇷'},
    'animals': {'name': 'Animals', 'emoji': '🐾'},
    'colours': {'name': 'Colours', 'emoji': '🎨'},
    'body': {'name': 'Body Parts', 'emoji': '🧑'},
    'food_kids': {'name': 'Food', 'emoji': '🍎'},
    'sentence_frames': {'name': 'Sentence Frames', 'emoji': '💬'},
    'podcast': {'name': 'Coffee Break French', 'emoji': '☕'},
}


@app.route('/')
def home():
    """Home page - user selection."""
    users = get_all_users()

    # Add stats for each user
    for user in users:
        stats = get_review_stats(user['name'])
        user['cards_learned'] = stats['cards_learned']
        user['cards_due'] = stats['cards_due']
        from progress import get_learning_streak
        streak = get_learning_streak(user['name'])
        user['current_streak'] = streak['current_streak']

    return render_template('home.html', users=users)


@app.route('/user/<name>')
def user_dashboard(name):
    """User dashboard with categories."""
    user = get_or_create_user(name)
    categories = get_categories()
    quiz_categories = get_quiz_categories()

    # Enrich categories with display info and progress
    for cat in categories:
        cat_name = cat['category']
        info = CATEGORY_INFO.get(cat_name, {'name': cat_name.title(), 'emoji': '📚'})
        cat['name'] = info['name']
        cat['emoji'] = info['emoji']
        cat['is_quiz'] = cat_name in quiz_categories

        # Get priority status for this category
        priority_status = get_priority_status(name, cat_name)
        cat['tiers'] = priority_status

        # Count due cards
        due_cards = get_due_cards(name, category=cat_name, limit=100)
        cat['due_count'] = len(due_cards)

    stats = get_review_stats(name)

    return render_template('categories.html',
                         user=user,
                         categories=categories,
                         stats=stats)


@app.route('/user/<name>/category/<cat>')
def category_detail(name, cat):
    """Category detail view with tier progress."""
    user = get_or_create_user(name)
    priority_status = get_priority_status(name, cat)

    info = CATEGORY_INFO.get(cat, {'name': cat.title(), 'emoji': '📚'})
    category_data = {
        'category': cat,
        'name': info['name'],
        'emoji': info['emoji'],
        'tiers': priority_status
    }

    return render_template('category_detail.html',
                         user=user,
                         category=category_data)


@app.route('/user/<name>/flashcard/<cat>')
def flashcard_mode(name, cat):
    """Flashcard study mode."""
    user = get_or_create_user(name)
    due_cards = get_due_cards(name, category=cat, limit=50)

    info = CATEGORY_INFO.get(cat, {'name': cat.title(), 'emoji': '📚'})

    return render_template('flashcard.html',
                         user=user,
                         category=cat,
                         category_name=info['name'],
                         category_emoji=info['emoji'],
                         cards=due_cards,
                         total_due=len(due_cards))


@app.route('/user/<name>/flashcard/review', methods=['POST'])
def submit_review(name):
    """Submit flashcard review (AJAX)."""
    data = request.get_json()
    card_id = data.get('card_id')
    quality = data.get('quality')

    if card_id is None or quality is None:
        return jsonify({'error': 'Missing card_id or quality'}), 400

    result = review_card(name, card_id, quality)
    return jsonify(result)


@app.route('/user/<name>/quiz/<cat>')
def quiz_mode(name, cat):
    """Picture quiz mode."""
    user = get_or_create_user(name)

    quiz_cats = get_quiz_categories()
    if cat not in quiz_cats:
        return redirect(url_for('user_dashboard', name=name))

    info = CATEGORY_INFO.get(cat, {'name': cat.title(), 'emoji': '📚'})

    return render_template('quiz.html',
                         user=user,
                         category=cat,
                         category_name=info['name'],
                         category_emoji=info['emoji'],
                         is_family=(name == 'Family'))


@app.route('/user/<name>/quiz/question/<cat>')
def get_quiz(name, cat):
    """Get a quiz question (AJAX)."""
    question = get_quiz_question(name, cat)

    if question is None:
        return jsonify({'error': 'Not enough cards for quiz'}), 400

    return jsonify(question)


@app.route('/user/<name>/quiz/answer', methods=['POST'])
def submit_quiz_answer(name):
    """Submit quiz answer (AJAX)."""
    data = request.get_json()
    card_id = data.get('card_id')
    correct = data.get('correct')

    if card_id is None or correct is None:
        return jsonify({'error': 'Missing card_id or correct'}), 400

    result = answer_quiz(name, card_id, correct)
    return jsonify(result)


@app.route('/user/<name>/progress')
def progress_page(name):
    """Full progress page."""
    user = get_or_create_user(name)
    summary = get_summary(name)
    daily_reviews = get_daily_reviews(name, days=30)
    difficult = get_difficult_cards(name, limit=10)
    mastered = get_mastered_cards(name, limit=10)

    return render_template('progress.html',
                         user=user,
                         summary=summary,
                         daily_reviews=daily_reviews,
                         difficult_cards=difficult,
                         mastered_cards=mastered)


@app.route('/api/users')
def api_users():
    """API: Get all users."""
    return jsonify(get_all_users())


@app.route('/api/user/<name>/stats')
def api_user_stats(name):
    """API: Get user stats."""
    return jsonify(get_review_stats(name))


if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG', 'true').lower() == 'true'
    app.run(debug=debug, port=5001)
