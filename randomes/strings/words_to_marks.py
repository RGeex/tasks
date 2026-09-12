"""
Если　a = 1, b = 2, c = 3 ... z = 26

Затемl + o + v + e = 54

иf + r + i + e + n + d + s + h + i + p = 108

Таким образом friendship, он в два раза сильнее, чем love:-)

Ваша задача — написать функцию, которая вычисляет значение слова на основе суммы позиций символов в алфавите.

Вводимые данные всегда будут состоять только из строчных букв и никогда не будут пустыми.
"""
import unittest
from typing import Any, Callable, Tuple


def words_to_marks(s: str) -> int:
    """
    Вычисляет значение слова на основе суммы позиций букв.
    """
    return sum(ord(x) - 96 for x in s)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(words_to_marks, (
        ('attitude', 100),
        ('friends', 75),
        ('family', 66),
        ('selfness', 99),
        ('knowledge', 96),
    ))
