"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Demonstrate importing and calling reusable core logic."""
    print(choose_action(position=1, goal=4))
    print(choose_action(position=4, goal=4))
    print(choose_action(position=7, goal=4))


if __name__ == "__main__":
    main()
