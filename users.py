"""
User Management Module
======================
Manage multiple users/accounts for the French learning app.
"""

from database import get_connection, init_db

# Default users to create
DEFAULT_USERS = ["Jack", "Nicola", "Family"]


def create_user(name: str) -> int:
    """
    Create a new user.

    Args:
        name: User's name

    Returns:
        int: User ID
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO users (name) VALUES (?)", (name,))
    conn.commit()

    cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
    user_id = cursor.fetchone()['id']
    conn.close()

    return user_id


def get_user(name: str) -> dict:
    """
    Get a user by name.

    Args:
        name: User's name

    Returns:
        dict: User data or None
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


def get_user_by_id(user_id: int) -> dict:
    """Get a user by ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


def get_all_users() -> list:
    """Get all users."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ORDER BY name")
    users = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return users


def delete_user(name: str) -> bool:
    """
    Delete a user and all their progress.

    Args:
        name: User's name

    Returns:
        bool: True if deleted
    """
    user = get_user(name)
    if not user:
        return False

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM review_history WHERE user_id = ?", (user['id'],))
    cursor.execute("DELETE FROM progress WHERE user_id = ?", (user['id'],))
    cursor.execute("DELETE FROM users WHERE id = ?", (user['id'],))

    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()

    return deleted


def get_or_create_user(name: str) -> dict:
    """
    Get a user by name, creating if doesn't exist.

    Args:
        name: User's name

    Returns:
        dict: User data
    """
    user = get_user(name)
    if not user:
        create_user(name)
        user = get_user(name)
    return user


def setup_default_users():
    """Create the default users if they don't exist."""
    for name in DEFAULT_USERS:
        create_user(name)


def user_count() -> int:
    """Get total number of users."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return count


# Auto-setup default users if none exist
if user_count() == 0:
    setup_default_users()
