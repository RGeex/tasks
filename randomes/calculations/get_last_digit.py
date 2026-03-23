"""

Как вы, вероятно, знаете, последовательность Фибоначчи — это числа из следующей
последовательности целых чисел: 1, 1, 2, 3, 5, 8, 13... Напишите метод, который
принимает индекс в качестве аргумента и возвращает последнюю цифру числа Фибоначчи.
Пример: getLastDigit(15) - 610. Ваш метод должен возвращать 0, потому что последняя
цифра числа 610 равна 0. Последовательность Фибоначчи растет очень быстро, и значение
может принимать очень большие числа (больше, чем может вместить целочисленный тип),
поэтому, пожалуйста, будьте осторожны с переполнением. 

"""
import unittest
from typing import Any, Callable, Tuple


def get_last_digit(n: int) -> int:
    """
    Определяет поаследнюю цифру в последовательности фибоначи по индексу элемента.
    """
    x = [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0]
    return (10 - x[(n - 1) % 30]) % 10 if (n - 1) % 60 >= 30 else x[(n - 1) % 30]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_last_digit, (
        (1, 1),
        (21, 6),
        (302, 1),
        (4003, 7),
        (50004, 8),
    ))
