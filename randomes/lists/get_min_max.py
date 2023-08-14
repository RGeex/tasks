"""
Реализуйте функцию, которая возвращает минимальное и максимальное
значение списка (в указанном порядке).
"""


def get_min_max(seq: list[int]) -> tuple:
    """Получение минимального и максимального значения из списка"""
    return tuple(sorted(seq * (len(seq) - 1 and 1 or 2)))[::len(seq) - 1 or 1]


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ([1], (1, 1)),
        ([1, 2], (1, 2)),
        ([2, 1], (1, 2)),
        ([2, 3, 1], (1, 3)),
    )
    for key, val in data:
        assert get_min_max(key) == val


if __name__ == '__main__':
    test()