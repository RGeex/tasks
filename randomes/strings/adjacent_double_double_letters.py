"""
Если задана строка, которая является словом, вернуть True,
если слово содержит смежные двойные двойные буквы, как в 'balloon'.

Например,

'balloon' -> True, 'lloo'являются смежными двойными двойными буквами

'baaloon' -> False, потому что, хотя есть две двойные буквы, они не являются соседними

'baboonn' -> True, здесь 'oonn'являются смежными двойными двойными буквами

'matte'   -> False, потому что есть только одна пара двойных букв

'aaaaaaah'  -> True, любая подстрока 'aaaa'делает его словом с соседними двойными буквами

Примечание: все слова будут написаны строчными буквами, без каких-либо символов и пробелов.

"""
import typing
import unittest
import re


def adjacent_double_double_letters(word: str) -> bool:
    """
    Определят находятся ли в слове 2 раза подряд 2 идущие подряд буквы.
    """
    return bool(re.findall(r'(.)\1(.)\2', word))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(adjacent_double_double_letters, (
        ('hello', False),
        ('helloo', True),
        ('hellouououuo', False),
        ('hheelloo', True),
        ('balloon', True),
        ('baalon', False),
    ))
