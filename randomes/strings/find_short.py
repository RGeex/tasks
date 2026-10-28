"""
Проще говоря, имея строку слов, нужно вернуть длину самого короткого слова (или слов).

Строка никогда не будет пустой, и вам не нужно учитывать разные типы данных.
"""
import unittest
from typing import Any, Callable, Tuple


def find_short(s: str) -> int:
    """
    Определяет длину самого короткого слова в строке.
    """
    return len(min(s.split(), key=len))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_short, (
        ("bitcoin take over the world maybe who knows perhaps", 3),
        ("turns out random test cases are easier than writing out basic ones", 3),
        ("lets talk about javascript the best language", 3),
        ("i want to travel the world writing code one day", 1),
        ("Lets all go on holiday somewhere very cold", 2)   ,
        ("Let's travel abroad shall we", 2),
    ))
