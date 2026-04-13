"""
Возьмите 2 струны s1 и s2включая только письма от a к z. Возвращает новую отсортированную строку
(в алфавитном порядке по возрастанию), максимально возможную длину, содержащую различные буквы —
каждая из которых встречается только один раз — из s1 или s2.
Примеры:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
import unittest
from typing import Any, Callable, Tuple


def longest(a1: str, a2: str) -> str:
    """
    Сортирует строки алфавиту, оставляя уникальные значений.
    """
    return ''.join(sorted(set(a1 + a2)))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(longest, (
        (("aretheyhere", "yestheyarehere"), "aehrsty"),
        (("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu"),
        (("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy"),
    ))
