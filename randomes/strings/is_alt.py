"""
Создать функцию isAlt() который принимает строку в качестве аргумента и
проверяет, находятся ли гласные (a, e, i, o, u) и согласные в
чередующемся порядке.

is_alt("amazon")  # True
is_alt("apple")   # False
is_alt("banana")  # True

Аргументы состоят только из строчных букв.
"""


def is_alt(s: str) -> bool:
    """
    Проверяет слово, чередуются ли в ней согласные и гласные.
    """
    return len({(w in 'aeiou') == i % 2 for i, w in enumerate(s)}) == 1


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("amazon", True),
        ("apple", False),
        ("banana", True),
        ("orange", False),
        ("helipad", True),
        ("yay", True),
    )
    for key, val in data:
        assert is_alt(key) == val


if __name__ == '__main__':
    test()
