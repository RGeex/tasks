"""
Напишите функцию, которая принимает одну строку (слово) в качестве аргумента.
Функция должна возвращать упорядоченный список, содержащий индексы всех
заглавных букв в строке.
"""


def capitals(word: str) -> list[int]:
    """
    Возвращает индексы заглавных букв в строке.
    """
    return [i for i, w in enumerate(word) if w.isupper()]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('CodEWaRs', [0, 3, 4, 6]),
    )
    for key, val in data:
        assert capitals(key) == val


if __name__ == '__main__':
    test()
