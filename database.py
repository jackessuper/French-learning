"""
Database module for French Learning App
=======================================
Handles SQLite database setup and connections.
"""

import os
import sqlite3
from pathlib import Path

# Use environment variable for DB path, with fallback to local file
DB_PATH = Path(os.environ.get('FRENCH_LEARNING_DB', Path(__file__).parent / "french_learning.db"))


def get_connection():
    """Get a database connection with row factory enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database schema."""
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Vocabulary cards table (shared across all users)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL DEFAULT 'general',
            topic TEXT NOT NULL,
            french TEXT NOT NULL,
            english TEXT NOT NULL,
            pronunciation TEXT,
            priority INTEGER DEFAULT 1,
            image TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Progress tracking table (per user, per card)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            card_id INTEGER NOT NULL,
            ease_factor REAL DEFAULT 2.5,
            interval INTEGER DEFAULT 0,
            repetitions INTEGER DEFAULT 0,
            next_review DATE,
            last_reviewed TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (card_id) REFERENCES cards(id),
            UNIQUE(user_id, card_id)
        )
    """)

    # Review history table (per user)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS review_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            card_id INTEGER NOT NULL,
            quality INTEGER NOT NULL,
            reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (card_id) REFERENCES cards(id)
        )
    """)

    conn.commit()
    conn.close()


def migrate_db():
    """Run database migrations for schema updates."""
    conn = get_connection()
    cursor = conn.cursor()

    # Check if image column exists
    cursor.execute("PRAGMA table_info(cards)")
    columns = [row['name'] for row in cursor.fetchall()]

    if 'image' not in columns:
        cursor.execute("ALTER TABLE cards ADD COLUMN image TEXT")
        conn.commit()

    conn.close()


def reset_db():
    """Reset the database (delete all data)."""
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()


# Initialize database on module import
init_db()
