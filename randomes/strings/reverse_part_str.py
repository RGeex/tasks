"""
В этом задании вам будет дана строка и два индекса ( a и bВаша задача — перевернуть
ту часть строки, которая находится между этими двумя индексами включительно.

str = "codewars", a = 1, b = 5 --> "cawedors"
str = "cODEWArs", a = 1, b = 5 --> "cAWEDOrs"

Вводимые данные будут содержать только строчные и заглавные буквы.

первый указатель aвсегда будет меньше длины строки; второй индекс bМожет быть больше длины строки.
Больше примеров в тестовых случаях. Удачи!
"""
import unittest
from typing import Any, Callable, Tuple


def reverse_part_str(st: str, a: int, b: int) -> str:
    """
    Переворачивает заданную часть строки.
    """
    return st[:a] + st[a:b + 1][::-1] + st[b + 1:]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_part_str, (
        (("codewars", 1, 5), "cawedors"),
        (("codingIsFun", 2, 100), "conuFsIgnid"),
        (("FunctionalProgramming", 2, 15), "FuargorPlanoitcnmming"),
        (("abcefghijklmnopqrstuvwxyz", 0, 20), "vutsrqponmlkjihgfecbawxyz"),
        (("abcefghijklmnopqrstuvwxyz", 5, 20), "abcefvutsrqponmlkjihgwxyz"),
    ))
