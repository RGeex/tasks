"""
Вы собираетесь в путешествие с несколькими студентами, и вам нужно следить за
тем, сколько денег есть у каждого студента. Студент определяется так:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

Как вы можете заметить, у каждого Студента есть пятёрки, десятки и двадцатки.
Ваша задача — вернуть имя студента, у которого больше всего денег. Если у
каждого ученика одинаковая сумма, то вернуть "all".

Примечания:

    У каждого ученика будет уникальное имя
    Всегда будет явный победитель: либо у одного человека больше, либо у всех
    одинаковое количество.
    Если есть только один студент, то у этого студента больше всего денег.
"""


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students: list[Student]) -> str:
    """
    Поиск студента с максимальным кол-вом денег.
    """
    x = {sum(getattr(x, a) * b for a, b in zip('fives tens twenties'.split(), [5, 10, 20])): x.name for x in students}
    return 'all' if len(x) == 1 and len(students) != 1 else max(x.items())[1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    students = [
        Student("Phil", 2, 2, 1),
        Student("Cameron", 2, 2, 0),
        Student("Geoff", 0, 3, 0),
    ]

    data = (
        (students, "Phil"),
        (students[1:], "all"),
        (students[2:], "Geoff"),
    )
    for key, val in data:
        assert most_money(key) == val


if __name__ == '__main__':
    test()
