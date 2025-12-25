"""
Если задано неотрицательное целое число, верните массив/список отдельных цифр в порядке
их следования.

Примеры:

123 => [1,2,3]

1 => [1]

8675309 => [8,6,7,5,3,0,9]

"""
import unittest
from typing import Any, Callable, List, Tuple


def digitize(n: int) -> List[int]:
    """
    Разбивает число на цифры и создает из них список.
    """
    return list(map(int, str(n)))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(digitize, (
        (123, [1, 2, 3]),
        (1, [1]),
        (0, [0]),
        (1230, [1, 2, 3, 0]),
        (8675309, [8, 6, 7, 5, 3, 0, 9]),
    ))
