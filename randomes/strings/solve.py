"""
Вернуть массив соответствия:
колличество букв стоящих в слове на местах как в алфавите.
"""


def solve(arr: list[str]) -> list[int]:
    """Поиск в списке слов, кол-ва букв стоящих на местах как в алфавите."""
    return [sum(chr(i + 97) == v for i, v in enumerate(w[:26].lower())) for w in arr]


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        (["abide", "ABc", "xyz"], [4, 3, 0]),
        (["abode", "ABc", "xyzD"], [4, 3, 1]),
        (["encode", "abc", "xyzD", "ABmD"], [1, 3, 1, 3]),
        (["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"], [6, 5, 7]),
    )

    for key, val in data:
        assert solve(key) == val


if __name__ == '__main__':
    test()
