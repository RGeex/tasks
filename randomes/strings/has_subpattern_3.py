"""
В этой Kata вам нужно построить функцию, чтобы вернуть либо true/True или false/False Если строка
можно рассматривать как повторение более простого/более короткого подчинения или нет.

Например:

has_subpattern("a") == False #no repeated pattern
has_subpattern("aaaa") == True #created repeating "a"
has_subpattern("abcd") == False #no repeated pattern
has_subpattern("abababab") == True #created repeating "ab"
has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern

Строки никогда не будут пустыми и могут быть составлены из любого персонажа (просто рассмотрите
верхние и строчные буквы как разные сущности) и могут быть довольно длинными
(следите за выступлениями!).
"""
import typing
import unittest


def has_subpattern(st: str) -> bool:
    """
    Проверяет, состоит ли строка из повторяющихся подстрок.
    """
    return not next((0 for i in range(1, len(st) + 1) if st[i:] and not st[i:].replace(st[:i], '')), 1)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(has_subpattern, (
        ("a", False),
        ("aaaa", True),
        ("abcd", False),
        ("abababab", True),
        ("ababababa", False),
        ("123a123a123a", True),
        ("123A123a123a", False),
        ("abbaabbaabba", True),
        ("abbabbabba", False),
        ("abcdabcabcd", False),
    ))
