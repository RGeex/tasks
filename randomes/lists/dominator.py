"""
Массив с нулевым индексом arrДан массив, состоящий из n целых чисел.
Доминатор массива arr— это значение, которое встречается более чем в половине элементов arr.
Например, рассмотрим массив. arrтаким образом, что arr = [3,4,3,2,3,1,3,3]
Доминатор arrЧисло равно 3, потому что оно встречается в 5 из 8 элементов. arrи 5 больше половины 8.
Напишите функцию dominator(arr)что, если задан массив с нулевой индексацией arrсостоит из n целых
чисел, возвращает доминант arrФункция должна возвращать −1, если массив не содержит доминатора.
Все значения в arrбудет >=0.
"""
import unittest
from typing import Any, Callable, List, Tuple
from collections import Counter


def dominator(arr: List[int]) -> int:
    """
    Определяет доминатор, если таковой имеется с массиве.
    """
    return next((k for k, v in Counter(arr).items() if v > len(arr) // 2), -1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(dominator, (
        ([3, 4, 3, 2, 3, 1, 3, 3], 3),
        ([1, 2, 3, 4, 5], -1),
        ([1, 1, 1, 2, 2, 2], -1),
        ([1, 1, 1, 2, 2, 2, 2], 2),
        ([], -1),
    ))
