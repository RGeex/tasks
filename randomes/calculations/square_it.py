"""
Если задано целое число, и длина его цифр является полным квадратом, верните квадратный блок
размером sqroot(length) * sqroot(length). В противном случае просто верните "Не является полным квадратом!".

Примеры:

1212возвраты:

"12
12"
Примечание: 4 цифры, следовательно, 2 в квадрате (2х2 — идеальный квадрат). По 2 цифры в каждой строке.

123123123возвраты:

"123
123
123"
Примечание: 9 цифр, следовательно, 3 в квадрате (3х3 — идеальный квадрат). 3 цифры в каждой строке.
"""
import unittest
from typing import Any, Callable, Tuple


def square_it(n: int) -> str:
    """
    Из заданного числа пытается сделать квадратный блок, если это возможно.
    """
    return len(str(n)) ** .5 % 1 and "Not a perfect square!" or '\n'.join(map(''.join, zip(*[iter(str(n))] * int(len(str(n)) ** .5))))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(square_it, (
        (1, '1'),
        (222, 'Not a perfect square!'),
        (1212, '12\n12'),
        (123123123, '123\n123\n123'),
        (234562342342, 'Not a perfect square!'),
        (88989, 'Not a perfect square!'),
        (112141568, '112\n141\n568'),
    ))
