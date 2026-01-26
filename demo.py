"""
Demo script to test the French Learning backend with categories and quiz.
Run: python3 demo.py
"""

from vocabulary import get_categories, get_priorities, card_count, reset_vocabulary
from spaced_repetition import review_card, get_due_cards, get_priority_status
from progress import compare_users
from users import get_all_users, setup_default_users
from database import reset_db
from quiz import get_quiz_categories, get_quiz_question, answer_quiz, get_quiz_stats, get_category_info


def show_category_status(user: str, category: str, emoji: str):
    """Display status for a category."""
    print(f"\n  {emoji} {category.upper()}")
    for status in get_priority_status(user, category):
        lock = "✅" if status['unlocked'] else "🔒"
        print(f"    {lock} P{status['priority']}: {status['reviewed']}/{status['total']} "
              f"({status['review_rate']}%)")


def main():
    print("=" * 60)
    print("  French Learning - Categories Demo")
    print("=" * 60)

    # Show categories
    print("\n📚 Categories:")
    for cat in get_categories():
        print(f"   • {cat['category']}: {cat['count']} cards")

    # Show users
    print("\n👥 Users:")
    for user in get_all_users():
        print(f"   • {user['name']}")

    # Show Jack's status by category
    print("\n" + "─" * 60)
    print("  👤 Jack's Progress")
    print("─" * 60)

    show_category_status("Jack", "general", "🇫🇷")
    show_category_status("Jack", "animals", "🐾")

    # Show due cards by category
    print("\n  📋 Due cards:")
    general_due = get_due_cards("Jack", category="general", limit=5)
    animals_due = get_due_cards("Jack", category="animals", limit=5)

    print(f"    General French: {len(get_due_cards('Jack', category='general', limit=100))} due")
    for card in general_due[:3]:
        print(f"      • {card['french']} = {card['english']}")

    print(f"    Animals: {len(get_due_cards('Jack', category='animals', limit=100))} due")
    for card in animals_due[:3]:
        print(f"      • {card['french']} = {card['english']}")

    # Simulate learning session
    print("\n" + "─" * 60)
    print("  📝 Jack learns some General French...")
    print("─" * 60)

    for card in general_due[:5]:
        result = review_card("Jack", card['id'], quality=4)
        print(f"    ✓ '{card['french']}' → next in {result['interval']} day(s)")

    print("\n  📝 Jack learns some Animals...")
    for card in animals_due[:3]:
        result = review_card("Jack", card['id'], quality=5)
        print(f"    ✓ '{card['french']}' → next in {result['interval']} day(s)")

    # Show updated status
    print("\n" + "─" * 60)
    print("  📊 Updated Status")
    print("─" * 60)
    show_category_status("Jack", "general", "🇫🇷")
    show_category_status("Jack", "animals", "🐾")

    print("\n" + "=" * 60)
    print("  Categories working!")
    print("=" * 60)

    # Picture Quiz Demo
    print("\n" + "=" * 60)
    print("  Picture Quiz Demo (Kid Mode)")
    print("=" * 60)

    print("\n  Quiz Categories:")
    for cat in get_quiz_categories():
        info = get_category_info(cat)
        print(f"    {info['emoji']} {info['name']}: {info['card_count']} picture cards")

    # Demo a quiz question
    print("\n" + "-" * 60)
    print("  Sample Quiz Question")
    print("-" * 60)

    question = get_quiz_question("Jack", "animals")
    if question:
        print(f"\n  Question: What is '{question['card']['french']}'?")
        print(f"  (Answer: {question['card']['english']})")
        print(f"\n  Options:")
        for i, opt in enumerate(question['options']):
            marker = " -> " if i == question['correct_index'] else "    "
            print(f"  {marker}[{i+1}] {opt['image']}")

        # Simulate correct answer
        print("\n  Jack answers correctly...")
        result = answer_quiz("Jack", question['card']['id'], correct=True)
        print(f"    Next review in {result['interval']} day(s)")

    # Demo incorrect answer
    question2 = get_quiz_question("Jack", "food_kids")
    if question2:
        print(f"\n  Question: What is '{question2['card']['french']}'?")
        print("  Jack answers incorrectly...")
        result2 = answer_quiz("Jack", question2['card']['id'], correct=False)
        print(f"    Will review again in {result2['interval']} day(s)")

    # Show quiz stats
    print("\n" + "-" * 60)
    print("  Quiz Stats for Jack")
    print("-" * 60)

    for cat in get_quiz_categories():
        stats = get_quiz_stats("Jack", cat)
        info = get_category_info(cat)
        print(f"  {info['emoji']} {info['name']}: {stats['reviewed']}/{stats['total_cards']} "
              f"reviewed ({stats['progress_percent']}%)")

    print("\n" + "=" * 60)
    print("  Quiz System Working!")
    print("=" * 60)

    print("\nQuiz Usage:")
    print("  # Get quiz categories")
    print("  get_quiz_categories()")
    print()
    print("  # Generate a quiz question")
    print("  question = get_quiz_question('Jack', 'animals')")
    print()
    print("  # Submit answer (updates spaced repetition)")
    print("  answer_quiz('Jack', card_id, correct=True)")
    print()
    print("  # Get quiz stats")
    print("  get_quiz_stats('Jack', 'animals')")


if __name__ == '__main__':
    print("Resetting database with categories...\n")
    reset_db()
    setup_default_users()
    from vocabulary import load_default_vocabulary
    load_default_vocabulary()

    main()
