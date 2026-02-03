"""
Рик хочет найти более быстрый способ вычисления произведения наибольшей пары чисел в массиве.
Ваша задача — создать производительное решение для нахождения произведения двух наибольших
целых чисел в уникальном массиве положительных чисел.
Все введенные данные будут действительными.
Передача [2, 6, 3] должна вернуть 18, произведение [6, 3].

Disclaimer: only accepts solutions that are faster than his, which has a running time O(nlogn).

max_product([2, 1, 5, 0, 4, 3])              # => 20
max_product([7, 8, 9])                       # => 72
max_product([33, 231, 454, 11, 9, 99, 57])   # => 104874
"""
import unittest
from typing import Any, Callable, List, Tuple


def max_product(arr: List) -> int:
    """
    Поиск произведения 2-х максимальных чисел из списка.
    """
    a = max(arr)
    arr.remove(a)
    return a * max(arr)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_product, (
        ([56, 335, 195, 443, 6, 494, 252], 218842),
        ([154, 428, 455, 346], 194740),
        ([39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411], 187827),
        ([136, 376, 10, 146, 105, 63, 234], 87984),
        ([354, 463, 165, 62, 472, 53, 347, 293, 252, 378, 420, 398, 255, 89], 218536),
        ([346, 446, 26, 425, 432, 349, 123, 269, 285, 93, 75, 14], 192672),
        ([134, 320, 266, 299], 95680),
        ([114, 424, 53, 272, 128, 215, 25, 329, 272, 313, 100, 24, 252], 139496),
        ([375, 56, 337, 466, 203], 174750),
    ))
