"""
Напишите функцию, которая принимает список, состоящий из других списков целых чисел,
и возвращает сумму всех чисел, встречающихся в двух или более списках входного списка.
Возможно, это звучит странно, но это не так:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9
"""
import unittest
from typing import Any, Callable, Tuple


def repeat_sum(l: list[list[int]]) -> int:
    """
    Вычисляет сумму дублирующихся элементов.
    """
    res = {}
    for a in l:
        for b in set(a):
            res[b] = res.get(b, 0) + 1
    return sum([n for n, x in res.items() if x > 1])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(repeat_sum, (
        ([[1, 2, 3], [2, 8, 9], [7, 123, 8]], 10),
        ([[1], [2], [3, 4, 4, 4], [123456789]], 0),
        ([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]], 9),
        ([[1]], 0),
    ))
