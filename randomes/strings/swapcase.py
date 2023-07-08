"""
Напишите функцию alterCase, которая переключает каждую
букву в строке с верхней на нижнюю и с нижней на верхнюю.
"""


def alternate_case(s: str):
    """Реализация swapcase"""
    return ''.join([x.lower(), x.upper()][x.islower()] for x in s)


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ("", ""),
        (" ", " "),
        ("ABC", "abc"),
        ("cODEwARS", "CodeWars"),
        ("Hello World", "hELLO wORLD"),
        ("i LIKE MAKING KATAS VERY MUCH", "I like making katas very much"),
    )

    for key, val in data:
        assert alternate_case(key) == val


if __name__ == '__main__':
    test()
