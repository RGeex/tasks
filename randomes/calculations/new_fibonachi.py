"""
При условии

f0 = '0'
f1 = '01'
f2 = '010' = f1 + f0
f3 = '01001' = f2 + f1
Вам будет дано число, и ваша задача — вернуть nthпоследовательность чисел Фибоначчи. Например:

solve(2) = '010'
solve(3) = '01001'
"""
import unittest
from typing import Any, Callable, Tuple


def new_fibonachi(n: int) -> str:
    """
    Последовательность фибоначи для заданного условия цепочки.
    """
    a, b = '01'
    for _ in range(n):
        a, b = a + b, a
    return a


def new_fibonachi_2(n: int) -> str:
    """
    Последовательность фибоначи для заданного условия цепочки.
    """
    return "0" if n == 0 else "01" if n == 1 else new_fibonachi_2(n-1) + new_fibonachi_2(n-2)


def new_fibonachi_3(n: int, f: str = '0', g: str = '01') -> str:
    """
    Последовательность фибоначи для заданного условия цепочки.
    """
    return new_fibonachi_3(n-1,g,g+f) if n else f


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(new_fibonachi, (
        (0,'0'),
        (1,'01'),
        (2,'010'),
        (3,'01001'),
        (5,'0100101001001'),
    ))
    test(new_fibonachi_2, (
        (0,'0'),
        (1,'01'),
        (2,'010'),
        (3,'01001'),
        (5,'0100101001001'),
    ))
    test(new_fibonachi_3, (
        (0,'0'),
        (1,'01'),
        (2,'010'),
        (3,'01001'),
        (5,'0100101001001'),
    ))
