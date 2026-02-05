"""
Нет истории

Нет описания

Только путем размышления и проверки.

Посмотрите на результаты тестовых случаев и попробуйте угадать код!
"""
import unittest
from typing import Any, Callable, Tuple


def testit(s: str) -> str:
    """
    Пишет каждое слово строки с заглавной буквы, но с конца с слова.
    """
    return s[::-1].title()[::-1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(testit, (
        ("", ""),
        ("a", "A"),
        ("b", "B"),
        ("a a", "A A"),
        ("a b", "A B"),
        ("a b c", "A B C"),
        ("abc", "abC"),
        ("abc abc", "abC abC"),
    ))
