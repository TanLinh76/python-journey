"""Ví dụ Week 14: class Student."""

class Student:
    """Đại diện cho một sinh viên."""

    def __init__(self, name: str, age: int, score: float) -> None:
        self.name = name
        self.age = age
        self.score = score

    def introduce(self) -> None:
        """In lời giới thiệu của sinh viên."""
        print(f"Tôi tên là {self.name}, {self.age} tuổi.")

    def show_score(self) -> None:
        """In điểm của sinh viên."""
        print(f"Điểm của tôi là {self.score}")


def main() -> None:
    student1 = Student("An", 18, 8.5)
    student2 = Student("Bình", 19, 9.0)

    student1.introduce()
    student1.show_score()

    student2.introduce()
    student2.show_score()


if __name__ == "__main__":
    main()
