"""
Состояние которые каждого элемента массива целых чисел определяется его позицией в массиве и
значениями других элементов массива. Состояние элемента E в массиве размером N определяется
путем сложения позиции P (0 <= P < N ) элемента в массиве и количества элементов массива,
E. меньше

Например, рассмотрим массив, содержащий целые числа: 6 9 3 8 2 3 1Статус элемента 8
Значение равно 8, потому что его позиция — 3, а в массиве 5 элементов меньше 8.

Вы вернёте элементы исходного массива в порядке возрастания статуса.
В случае, если два или более элементов имеют одинаковый статус, выведете их в
порядке появления в массиве.

ПРИМЕР:

status([6, 9, 3, 8, 2, 3, 1]) = [6, 3, 2, 1, 9, 3, 8]


"""
import unittest
from typing import Any, Callable, List, Tuple


def status(nums: List[int]) -> List[int]:
    """
    Сортирует массив по состоянию элементов.
    """
    return [x[-1] for x in sorted([(i + sum(1 for x in nums if x < n), i, n) for i, n in enumerate(nums)])]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(status, (
        ([6, 9, 3, 8, 2, 3, 1], [6, 3, 2, 1, 9, 3, 8]),
        ([5, 5, 5, 8, 7, -2, -2, -3, 1, 9, 8, 3, -3, 4, -4, 6], [5, -2, -3, 5, -2, 5, 1, -3, -4, 8, 7, 3, 4, 8, 9, 6]),
        ([14, -3, 4, 6, 9, 10, -2, 4, 0], [-3, 4, -2, 14, 6, 9, 4, 0, 10]),
    ))
