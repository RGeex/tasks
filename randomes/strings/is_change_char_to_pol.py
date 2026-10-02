"""
В этом задании вы проверите, возможно ли преобразовать строку в палиндром, изменив один символ.

Например:

solve ("abbx") = True, because we can convert 'x' to 'a' and get a palindrome. 
solve ("abba") = False, because we cannot get a palindrome by changing any character. 
solve ("abcba") = True. We can change the middle character. 
solve ("aa") = False 
solve ("ab") = True
Удачи!
"""
import unittest
from typing import Any, Callable, Tuple


def is_change_char_to_pol(s: str) -> bool:
    """
    Проверяет возможно ли изменив 1 символ сстроке стать палиндромом.
    """
    return (x := sum(a != b for a, b in zip(s, s[::-1]))) == 2 or (x == 0 and len(s) % 2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_change_char_to_pol, (
        ("abba", False),
        ("abbaa", True),
        ("abbx", True),
        ("aa", False),
        ("ab", True),
        ("abcba", True),
    ))
