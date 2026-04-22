"""
    Входные данные: массив целых чисел.

    Результат: этот массив, но отсортированный таким образом, что в нем два крыла:

    Левое крыло с уменьшающейся численностью,

    Правое крыло, численность которого увеличивается.

    Длина обоих крыльев одинакова. Если длина массива нечетная, то... Крылья расположены у
    основания, если длина одинакова, то основание находится... Считается частью правого крыла.

    каждое целое число lЗначение левого крыла должно быть больше или равно значению его
    соответствующего значения. rна правом фланге, разница l - rбыть как можно меньше.
    Иными словами, правое крыло должно быть почти таким же крутым, как и левое.

Функция заключается в следующем: make_valley or makeValley or make-valley.

a = [79, 35, 54, 19, 35, 25]
make_valley(a) --> [79, 35, 25, *19*, 35, 54]
The bottom is 19, left wing is [79, 35, 25], right wing is [*19*, 35, 54].
79..................54
    35..........35
        25. 
          ..19

a = [67, 93, 100, -16, 65, 97, 92]
make_valley(a) --> [100, 93, 67, *-16*, 65, 92, 97]
The bottom is -16, left wing [100, 93, 67] and right wing [65, 92, 97] have same length.
100.........................97
    93..........
               .........92
        67......
               .....65
            -16     

a = [66, 55, 100, 68, 46, -82, 12, 72, 12, 38]
make_valley(a) --> [100, 68, 55, 38, 12, *-82*, 12, 46, 66, 72]
The bottom is -82, left wing is [100, 68, 55, 38, 12]], right wing is [*-82*, 12, 46, 66, 72].

a = [14,14,14,14,7,14]
make_valley(a) => [14, 14, 14, *7*, 14, 14]

a = [14,14,14,14,14]
make_valley(a) => [14, 14, *14*, 14, 14]

Контрпример:

a = [17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]
A solution could be [17, 17, 15, 14, 8, 1, 4, 4, 5, 7, 7]
but the right wing [4, 4, 5, 7, 7] is much flatter than the left one 
[17, 17, 15, 14, 8].

Summing the differences between left and right wing:
(17-7)+(17-7)+(15-5)+(14-4)+(8-4) = 44

Consider the following solution:
[17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]
Summing the differences between left and right wing:
(17-17)+(15-14)+(8-7)+(7-5)+(4-4) = 4
The right wing is nearly as steep as the right one.
"""
import unittest
from typing import Any, Callable, List, Tuple


def make_valley(arr: List[int]) -> List[int]:
    """
    Сортирует список чилел заданным образом.
    """
    return [b for a in [[x for x in x if x][::i % 2 or -1] for i, x in enumerate(zip(*[[x, 0][::i % 2 or -1] for i, x in enumerate(sorted(arr)[::-1], 1)]), 1)] for b in a]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(make_valley, (
        ([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1], [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]),
        ([20, 7, 6, 2], [20, 6, 2, 7]),
        ([14, 10, 8], [14, 8, 10]),
        ([20, 18, 17, 13, 12, 12, 10, 9, 4, 2, 2, 1, 1], [20, 17, 12, 10, 4, 2, 1, 1, 2, 9, 12, 13, 18]),
        ([20, 16, 14, 10, 1], [20, 14, 1, 10, 16]),
        ([19, 19, 18, 14, 12, 11, 9, 7, 4], [19, 18, 12, 9, 4, 7, 11, 14, 19]),
        ([20, 18, 16, 15, 14, 14, 13, 13, 10, 9, 4, 4, 4, 1], [20, 16, 14, 13, 10, 4, 4, 1, 4, 9, 13, 14, 15, 18]),
        ([20, 20, 16, 14, 12, 12, 11, 10, 3, 2], [20, 16, 12, 11, 3, 2, 10, 12, 14, 20]),
        ([19, 17, 16, 15, 13, 8, 5, 5, 4, 4, 4], [19, 16, 13, 5, 4, 4, 4, 5, 8, 15, 17]),
        ([19, 8, 6], [19, 6, 8]),
    ))
