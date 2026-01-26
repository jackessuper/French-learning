"""
Progress Tracking Module
========================
Track learning progress, streaks, and statistics per user.
"""

from datetime import datetime, timedelta
from database import get_connection
from users import get_or_create_user


def get_learning_streak(user: str):
    """
    Calculate the current learning streak for a user.

    Args:
        user: User name

    Returns:
        dict: Current streak and longest streak
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT date(reviewed_at) as review_date
        FROM review_history
        WHERE user_id = ?
        ORDER BY review_date DESC
    """, (user_id,))
    dates = [row['review_date'] for row in cursor.fetchall()]
    conn.close()

    if not dates:
        return {'current_streak': 0, 'longest_streak': 0}

    # Calculate current streak
    current_streak = 0
    today = datetime.now().date()
    check_date = today

    for date_str in dates:
        review_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        if review_date == check_date or review_date == check_date - timedelta(days=1):
            current_streak += 1
            check_date = review_date - timedelta(days=1)
        else:
            break

    # Calculate longest streak
    if len(dates) <= 1:
        longest_streak = len(dates)
    else:
        longest_streak = 1
        current_run = 1
        for i in range(1, len(dates)):
            prev_date = datetime.strptime(dates[i-1], '%Y-%m-%d').date()
            curr_date = datetime.strptime(dates[i], '%Y-%m-%d').date()
            if prev_date - curr_date == timedelta(days=1):
                current_run += 1
                longest_streak = max(longest_streak, current_run)
            else:
                current_run = 1

    return {
        'current_streak': current_streak,
        'longest_streak': max(longest_streak, current_streak)
    }


def get_topic_progress(user: str):
    """
    Get progress breakdown by topic for a user.

    Args:
        user: User name

    Returns:
        dict: Progress stats for each topic
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().date().isoformat()

    cursor.execute("""
        SELECT
            c.topic,
            COUNT(c.id) as total_cards,
            COUNT(CASE WHEN p.repetitions > 0 THEN 1 END) as learned,
            COUNT(CASE WHEN p.next_review IS NULL OR p.next_review <= ? THEN 1 END) as due,
            AVG(CASE WHEN p.ease_factor IS NOT NULL THEN p.ease_factor END) as avg_ease
        FROM cards c
        LEFT JOIN progress p ON c.id = p.card_id AND p.user_id = ?
        GROUP BY c.topic
    """, (today, user_id))

    topics = {}
    for row in cursor.fetchall():
        topics[row['topic']] = {
            'total_cards': row['total_cards'],
            'learned': row['learned'] or 0,
            'due': row['due'] or 0,
            'mastery': round((row['learned'] or 0) / row['total_cards'] * 100, 1),
            'avg_ease': round(row['avg_ease'], 2) if row['avg_ease'] else 2.5
        }

    conn.close()
    return topics


def get_daily_reviews(user: str, days: int = 30):
    """
    Get review counts for the past N days for a user.

    Args:
        user: User name
        days: Number of days to look back

    Returns:
        list: Daily review counts
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date(reviewed_at) as date, COUNT(*) as count
        FROM review_history
        WHERE user_id = ? AND reviewed_at >= date('now', ?)
        GROUP BY date(reviewed_at)
        ORDER BY date
    """, (user_id, f'-{days} days'))

    reviews = {row['date']: row['count'] for row in cursor.fetchall()}
    conn.close()

    result = []
    for i in range(days, -1, -1):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        result.append({
            'date': date,
            'reviews': reviews.get(date, 0)
        })

    return result


def get_difficult_cards(user: str, limit: int = 10):
    """
    Get cards that the user struggles with.

    Args:
        user: User name
        limit: Maximum number of cards

    Returns:
        list: Cards with lowest ease factors
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.*, p.ease_factor, p.repetitions,
               (SELECT COUNT(*) FROM review_history h
                WHERE h.card_id = c.id AND h.user_id = ?) as total_reviews
        FROM cards c
        JOIN progress p ON c.id = p.card_id AND p.user_id = ?
        WHERE p.repetitions > 0
        ORDER BY p.ease_factor ASC
        LIMIT ?
    """, (user_id, user_id, limit))

    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return cards


def get_mastered_cards(user: str, limit: int = 10):
    """
    Get well-learned cards for a user.

    Args:
        user: User name
        limit: Maximum number of cards

    Returns:
        list: Best performing cards
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.*, p.ease_factor, p.interval, p.repetitions
        FROM cards c
        JOIN progress p ON c.id = p.card_id AND p.user_id = ?
        WHERE p.repetitions >= 3
        ORDER BY p.interval DESC, p.ease_factor DESC
        LIMIT ?
    """, (user_id, limit))

    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return cards


def get_review_quality_distribution(user: str):
    """
    Get distribution of review quality ratings for a user.

    Args:
        user: User name

    Returns:
        dict: Count of each quality rating
    """
    user_data = get_or_create_user(user)
    user_id = user_data['id']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT quality, COUNT(*) as count
        FROM review_history
        WHERE user_id = ?
        GROUP BY quality
        ORDER BY quality
    """, (user_id,))

    distribution = {i: 0 for i in range(6)}
    for row in cursor.fetchall():
        distribution[row['quality']] = row['count']

    conn.close()
    return distribution


def get_summary(user: str):
    """
    Get a complete learning summary for a user.

    Args:
        user: User name

    Returns:
        dict: Comprehensive progress summary
    """
    from spaced_repetition import get_review_stats

    stats = get_review_stats(user)
    streak = get_learning_streak(user)
    topics = get_topic_progress(user)
    quality = get_review_quality_distribution(user)

    total_reviews = sum(quality.values())
    if total_reviews > 0:
        avg_quality = sum(q * c for q, c in quality.items()) / total_reviews
        success_rate = sum(quality.get(q, 0) for q in [3, 4, 5]) / total_reviews * 100
    else:
        avg_quality = 0
        success_rate = 0

    return {
        'user': user,
        'cards': stats,
        'streak': streak,
        'topics': topics,
        'quality_distribution': quality,
        'average_quality': round(avg_quality, 2),
        'success_rate': round(success_rate, 1)
    }


def compare_users():
    """
    Compare progress across all users.

    Returns:
        list: Summary for each user
    """
    from users import get_all_users
    from spaced_repetition import get_review_stats

    users = get_all_users()
    comparison = []

    for user in users:
        name = user['name']
        stats = get_review_stats(name)
        streak = get_learning_streak(name)

        comparison.append({
            'name': name,
            'cards_learned': stats['cards_learned'],
            'cards_due': stats['cards_due'],
            'reviews_today': stats['reviews_today'],
            'current_streak': streak['current_streak'],
            'average_ease': stats['average_ease']
        })

    return comparison
