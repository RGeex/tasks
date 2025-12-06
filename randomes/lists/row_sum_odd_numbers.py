"""
Дан треугольник последовательных нечетных чисел:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Вычислите сумму чисел в n-м ряду. й строка этого треугольника (начиная с индекса 1), например:
( Вход --> Выход )

1 -->  1
2 --> 3 + 5 = 8


"""
import unittest
from typing import Any, Callable, Tuple


def row_sum_odd_numbers(n: int) -> int:
    """
    Определяет сумму чисел строки треугольника.
    """
    return (n ** 2 - n + 1) * n + (n - 1) ** 2 + n - 1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(row_sum_odd_numbers, (
        (1, 1),
        (2, 8),
        (13, 2197),
        (19, 6859),
        (41, 68921),
    ))
