"""
Вам дан массив, содержащий несколько элементов. "even"слова, одно "odd"слово,
и несколько чисел вперемешку.

Определите, является ли какое-либо из чисел в массиве индексом... "odd"слово.
Если да, то вернуть true, в противном случае false.

"""
import unittest
from typing import Any, Callable, List, Tuple


def odd_ball(arr: List[int | str]) -> bool:
    """
    Определяет, присутствует ли в массиве число являющееся индексом значения "odd".
    """
    return next((i in arr for i, x in enumerate(arr) if x == 'odd'), False)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(odd_ball, (
        (["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"], True),
        (["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"], False),
        (["even", 10, "odd", 2, "even"], True),
    ))
