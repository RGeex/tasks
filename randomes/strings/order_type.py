"""
Напишите функцию, которая принимает в качестве аргумента один массив
(содержащий несколько строк и/или положительные числа и/или массивы)
и возвращает одно из четырех возможных строковых значений, в
зависимости от порядка длин элементов во входном массиве:

Ваша функция должна вернуть...

    «По возрастанию» — если длины элементов увеличиваются слева направо
    (хотя возможно, что некоторые соседние элементы также могут быть равными по длине)
    «Убывающая» — если длины элементов уменьшаются слева направо
    (хотя возможно, что некоторые соседние элементы также могут быть равными по длине)
    «Несортированный» — если длины элементов колеблются слева направо
    «Константа» — если длины всех элементов одинаковы.

Числа и строки следует оценивать на основе количества символов или цифр,
используемых для их записи.

Массивы следует оценивать на основе количества элементов, подсчитанных
непосредственно в родительском массиве (а не количества элементов,
содержащихся в каких-либо подмассивах). 
"""


from typing import Any
from functools import reduce
from collections.abc import Iterable


def order_type(arr: list[Any]) -> str:
    """
    Проверяет являются ли элементы переданного списка по длине: возрастающими, убывающими или не изменяющимися.
    """
    res, x = [], [len(x if isinstance(x, Iterable) else str(x)) for x in arr]
    reduce(lambda a, b: res.append({a > b: 1, a < b: 2}.get(1, 0)) or b, x or [0])
    return ['Decreasing', 'Increasing'][x.pop() - 1] if len(x := set(filter(bool, res))) == 1 else ['Unsorted', 'Constant'][not x]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([1, "b", ["p"], 2],"Constant"),
        ([123, 1234, 12345, 123456],"Increasing"),
        (["a", "abc", "abcde", "ab"],"Unsorted"),
        ([[1, 2, 3, 4], [5, 6, 7], [8, 9]],"Decreasing"),
        ([1, 2, 3, 4, 56],"Increasing"),
        ([["ab","cdef", "g"],["hi","jk","lmnopq"],["rst", "uv", "wx"],["yz"]],"Decreasing"),
        ([[1, 23, 456, 78910], ["abcdef", "ghijklmno", "pqrstuvwxy"], [[1, 23, 456, 78910, ["abcdef", "ghijklmno", "pqrstuvwxy"]], 1234]],"Decreasing"),
        ([],"Constant"),
        (["pippi", "pippi", "batuffulo", "pippi"],"Unsorted"),
        (["pippi"],"Constant"),
    )
    for key, val in data:
        assert order_type(key) == val


if __name__ == '__main__':
    test()
