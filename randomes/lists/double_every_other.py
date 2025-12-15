"""
Напишите функцию, которая удваивает каждое второе целое число в списке, начиная слева.

Пример:

Для входного массива/списка:

[1,2,3,4]

Функция должна возвращать:

[1,4,3,8]


"""
import unittest
from typing import Any, Callable, Tuple


def double_every_other(lst: list[int]) -> list[int]:
    """
    Удваивает каждое второе число в списке.
    """
    return [x * [1, 2][i % 2] for i, x in enumerate(lst)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(double_every_other, (
        ([1,2,3,4,5], [1,4,3,8,5]),
        ([1,19,6,2,12,-3], [1,38,6,4,12,-6]),
        ([-1000,1653,210,0,1], [-1000,3306,210,0,1]),
    ))
