"""Exercise 02: add and validate an argparse option."""

import argparse


def parser() -> argparse.ArgumentParser:
    """Build the parser for a positive turn number."""
    result = argparse.ArgumentParser(description="Week 13 CLI exercise")
    result.add_argument(
        "--turn",
        type=int,
        required=True,
        help="Số lượt, phải là số nguyên dương",
    )
    return result


def main() -> int:
    """Parse learner arguments, validate turn and print the result."""
    args = parser().parse_args()
    if args.turn < 1:
        parser().error("--turn phải lớn hơn hoặc bằng 1")
    print(f"turn={args.turn}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
