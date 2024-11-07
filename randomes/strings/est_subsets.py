"""
Учитывая набор элементов (целые числа или строковые символы, символы только в RISC-V), где любой элемент может встречаться более одного раза, верните количество подмножеств, которые не содержат повторяющийся элемент.

Давайте посмотрим на примере:

set numbers = {1, 2, 3, 4}

Подмножества:

{{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}, {1,2,3},
{1,2,4}, {1,3,4}, {2,3,4}, {1,2,3,4}}

Есть 15 подмножеств. Как видите, пустой набор {} не учитывается.

Давайте посмотрим пример с повторениями элемента:

set letters = {a, b, c, d, d}

Подмножествами для этого случая (включая только те, которые не содержат
повторяющихся элементов внутри) будут:

{{a}, {b}, {c}, {d}, {a,b}, {a,c}, {a,d}, {b,c}, {b,d}, {c,d}, {a,b,c},
{a,b,d}, {a,c,d}, {b,c,d}, {a,b,c,d}}

Есть 15 подмножеств.

Функция est_subsets() (Яваскрипт: estSubsets()) вычислит количество этих
подмножеств.

Он получит массив в качестве аргумента и по его признакам выведет количество
подмножеств, не содержащих повторяющийся элемент.

est_subsets([1, 2, 3, 4]) == 15
est_subsets(['a', 'b', 'c', 'd', 'd']) == 15

Особенности случайных тестов:

Low Performance Tests: 40
Length of the arrays between 6 and 15

High Performance Tests: 80
Length of the arrays between 15 and 100 (Python and Ruby) between 15 and 63
(C++) and between 15 and 50 in javascript and Lua
"""


from typing import Any
from itertools import combinations as cb


def est_subsets_1(arr: list[Any]) -> int:
    """
    Подсчитывает кол-во уникальных подмножеств.
    """
    return sum(map(len, [list(cb(set(arr), i + 1)) for i in range(len(set(arr)))]))


def est_subsets_2(arr: list[Any]) -> int:
    """
    Подсчитывает кол-во уникальных подмножеств.
    """
    return 2 ** len(set(arr)) - 1


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([1, 2, 3, 4], 15),
        (['a', 'b', 'c', 'd', 'd'], 15),
        ([2, 3, 4, 5, 5, 6, 6, 7, 8, 8], 127),
        (['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 'd', 'j', 'j', 'n', 'm', 'm'], 511),
        ([1] * 8, 1),
        ([], 0),
    )
    for key, val in data:
        assert est_subsets_1(key) == val
        assert est_subsets_2(key) == val


if __name__ == '__main__':
    test()
