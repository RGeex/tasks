"""
Дан целочисленный список, необходимо вернуть список с отсортированными
не четными элементами, четные оставить на своих местах.
"""


def sort_array(source_array):
    """Возвращает исходный список с отсортированными тлько не четными числами,
    четные остаются на своих местах без изменений."""
    tmp = iter(sorted(i for i in source_array if i % 2))
    return [next(tmp) if i % 2 else i for i in source_array]


def test() -> None:
    """Тестирование работы алгоритмов."""
    lst1 = [5, 8, 6, 3, 4]
    lst2 = [3, 8, 6, 5, 4]
    lst3 = sort_array(lst1)

    assert lst2 == lst3


if __name__ == '__main__':
    test()
