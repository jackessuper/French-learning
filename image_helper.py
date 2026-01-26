"""
Image Helper Utility
====================
Downloads images for vocabulary cards that don't have emoji representation.
Uses free image APIs (Unsplash, Pixabay) to fetch appropriate images.

Usage:
    python3 image_helper.py

This will scan for cards without images and offer to download them.
"""

import os
import urllib.request
import urllib.parse
from pathlib import Path
from database import get_connection
from vocabulary import update_card

# Directory for downloaded images
IMAGES_DIR = Path(__file__).parent / "images"


def ensure_images_dir():
    """Create images directory if it doesn't exist."""
    IMAGES_DIR.mkdir(exist_ok=True)


def get_cards_without_images(category: str = None) -> list:
    """
    Get cards that don't have an image set.

    Args:
        category: Optional category filter

    Returns:
        list: Cards without images
    """
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("""
            SELECT * FROM cards
            WHERE image IS NULL AND category = ?
            ORDER BY priority, id
        """, (category,))
    else:
        cursor.execute("""
            SELECT * FROM cards
            WHERE image IS NULL
            ORDER BY category, priority, id
        """)

    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return cards


def download_image_unsplash(query: str, filename: str, access_key: str = None) -> str:
    """
    Download an image from Unsplash.

    Args:
        query: Search query for the image
        filename: Filename to save as (without extension)
        access_key: Unsplash API access key

    Returns:
        str: Path to downloaded image, or None if failed
    """
    if not access_key:
        print("Unsplash requires an API key. Get one at: https://unsplash.com/developers")
        return None

    ensure_images_dir()

    try:
        # Search for image
        search_url = f"https://api.unsplash.com/search/photos?query={urllib.parse.quote(query)}&per_page=1"
        req = urllib.request.Request(search_url)
        req.add_header('Authorization', f'Client-ID {access_key}')

        with urllib.request.urlopen(req) as response:
            import json
            data = json.loads(response.read().decode())

            if not data.get('results'):
                print(f"No images found for: {query}")
                return None

            # Get the small image URL
            image_url = data['results'][0]['urls']['small']

            # Download the image
            filepath = IMAGES_DIR / f"{filename}.jpg"
            urllib.request.urlretrieve(image_url, filepath)

            return str(filepath)

    except Exception as e:
        print(f"Error downloading image for '{query}': {e}")
        return None


def download_image_placeholder(query: str, filename: str) -> str:
    """
    Download a placeholder image (for testing/demo purposes).

    Args:
        query: Search query (used for placeholder text)
        filename: Filename to save as

    Returns:
        str: Path to downloaded image
    """
    ensure_images_dir()

    try:
        # Use a placeholder service
        text = urllib.parse.quote(query[:20])
        url = f"https://via.placeholder.com/200x200.png?text={text}"

        filepath = IMAGES_DIR / f"{filename}.png"
        urllib.request.urlretrieve(url, filepath)

        return str(filepath)

    except Exception as e:
        print(f"Error downloading placeholder for '{query}': {e}")
        return None


def set_card_image(card_id: int, image_path: str) -> bool:
    """
    Set the image path for a card.

    Args:
        card_id: Card ID
        image_path: Path to the image file

    Returns:
        bool: Success status
    """
    return update_card(card_id, image=image_path)


def list_missing_images(categories: list = None):
    """
    List all cards that are missing images.

    Args:
        categories: Optional list of categories to check
    """
    if categories is None:
        from quiz import QUIZ_CATEGORIES
        categories = QUIZ_CATEGORIES

    for category in categories:
        cards = get_cards_without_images(category)
        if cards:
            print(f"\n{category.upper()} - {len(cards)} cards without images:")
            for card in cards[:10]:  # Show first 10
                print(f"  - {card['french']} ({card['english']})")
            if len(cards) > 10:
                print(f"  ... and {len(cards) - 10} more")


def main():
    """Main function to run when script is executed directly."""
    print("=" * 60)
    print("  Image Helper - French Learning App")
    print("=" * 60)

    from quiz import QUIZ_CATEGORIES

    print("\nChecking for cards without images in quiz categories...")
    list_missing_images(QUIZ_CATEGORIES)

    print("\n" + "-" * 60)
    print("Options:")
    print("  1. Most quiz categories use emoji (no downloads needed)")
    print("  2. To add custom images, use set_card_image(card_id, path)")
    print("  3. For bulk downloads, provide an Unsplash API key")
    print("-" * 60)


if __name__ == '__main__':
    main()
