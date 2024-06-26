"""
Вам дан массив. Завершите функцию, которая возвращает количество ВСЕХ
элементов массива, включая любые вложенные массивы.
Примеры

[]                   -->  0
[1, 2, 3]            -->  3
["x", "y", ["z"]]    -->  4
[1, 2, [3, 4, [5]]]  -->  7

Входные данные всегда будут массивом.
"""


def deep_count(arr: list) -> int:
    """
    Определяет длинну списка, учитывая все вложенные списки.
    """
    return sum(deep_count(x) + 1 if isinstance(x, list) else 1 for x in arr)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([], 0),
        ([1, 2, 3], 3),
        (["x", "y", ["z"]], 4),
        ([1, 2, [3, 4, [5]]], 7),
        ([[[[[[[[[]]]]]]]]], 8),
    )
    for key, val in data:
        assert deep_count(key) == val


if __name__ == '__main__':
    test()
