"""
Сумма xпоследовательные целые числа — это yКакое последовательное целое число находится на позиции?
n? Данный x, y, и nРешите уравнение относительно целого числа.
Предположим, что начальная позиция равна 0.

Например, если сумма 4 последовательных целых чисел равна 14,
то какое последовательное целое число находится на третьей позиции?

Мы обнаруживаем, что последовательными целыми числами являются [2, 3, 4, 5]
Таким образом, целое число на позиции 3 равно 5.

position(4, 14, 3) == 5

Предположим, что сумма всегда будет равна xпоследовательные целые числа,
сумма которых равна y и n
Никогда не выйдет за пределы допустимого диапазона индексации.


"""
import unittest
from typing import Any, Callable, Tuple
from math import ceil


def position_1(x: int, y: int, n: int) -> int:
    """
    Определяет число последовательности на заданной позиции.
    """
    return list(range(k := ceil(y / x - x // 2), k + x))[n]


def position_2(x: int, y: int, n: int) -> int:
    """
    Определяет число последовательности на заданной позиции.
    """
    return (y - sum(range(x))) // x + n


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(position_1, (
        ((4, 14, 3), 5),
        ((2, 25, 0), 12),
        ((7, 749, 5), 109),
        ((3, -9, 1), -3),
        ((5, 0, 0), -2),
    ))
    test(position_2, (
        ((4, 14, 3), 5),
        ((2, 25, 0), 12),
        ((7, 749, 5), 109),
        ((3, -9, 1), -3),
        ((5, 0, 0), -2),
    ))
