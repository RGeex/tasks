"""
Напишите функцию, которая, получив заголовок столбца в формате Excel,
возвращает соответствующий номер столбца.

Все заголовки колонок будут написаны заглавными буквами.

Примеры:

Column title: "A" --> return 1
Column title: "Z" --> return 26
Column title: "AA" --> return 27
"""
import unittest
from typing import Any, Callable, Tuple


def title_to_number(title: str) -> int:
    """
    Определяетномер столбца в excel по его заголовку.
    """
    return sum(26 ** i * (ord(x) - 64) for i, x in enumerate(title[::-1]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(title_to_number, (
        ('A', 1),
        ('Z', 26),
        ('AA', 27),
        ('AZ', 52),
        ('BA', 53),
        ('CODEWARS', 28779382963),
        ('ZZZTOP', 321268054),
        ('OYAJI', 7294985),
        ('LONELINESS', 68400586976949),
        ('UNFORGIVABLE', 79089429845931757),
    ))
