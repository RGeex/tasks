"""
Найдите число n, чтобы получить последовательность от n до 1.
Число n может быть как отрицательным, так и большим. (Диапазон значений указан ниже)

Example : 
n=5  >> [5,4,3,2,1]
n=-1 >> [-1,0,1]

Range :
Python     -9999 < n < 9999
Javascript -9999 < n < 9999
c++        -9999 < n < 9999
Crystal    -9999 < n < 9999
Ruby       -9999 < n < 9999


"""
import unittest
from typing import Any, Callable, List, Tuple


def seq_to_one(n: int) -> List[int]:
    """
    Создает список от указанного числа до 1 включительно.
    """
    return list(range(n, 1, n <= 0 or -1)) + [1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(seq_to_one, (
        (5, [5, 4, 3, 2, 1]),
        (-1, [-1, 0, 1]),
    ))
