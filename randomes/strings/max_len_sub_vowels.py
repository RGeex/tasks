"""
Гласные подстроки в слове codewarriors являются o,e,a,io.
Самая длинная из них имеет длину 2. Если задана строка в нижнем регистре,
которая содержит только буквы алфавита (гласные и согласные) и не содержит пробелов,
верните длину самой длинной подстроки гласных. Гласные — это любые из aeiou.
"""
import typing
import unittest
from itertools import groupby


def max_len_sub_vowels(st: str) -> int:
    """
    Поиск максимальной длины подстроки с подряд идущими гласными.
    """
    return max([len(list(b)) for a, b in groupby(st, key=lambda x: x in 'aeiou') if a], default=0)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_len_sub_vowels, (
        ("", 0),
        ("codewarriors", 2),
        ("suoidea", 3),
        ("ultrarevolutionariees", 3),
        ("strengthlessnesses", 1),
        ("cuboideonavicuare", 2),
        ("chrononhotonthuooaos", 5),
        ("iiihoovaeaaaoougjyaw", 8),
    ))
