"""
Вам будет дано слово. Ваша работа заключается в том, чтобы убедиться, что каждый персонаж в этом словом имеет одинаковое количество случаев. Вы вернетесь true Если это действительно, или false Если это не так.

Для этой каты столицы считаются такими же, как и строчные буквы. Поэтому: "A" == "a"

Вход - это строка (без пробелов), содержащая [a-z],[A-Z],[0-9] и общие символы. Длина будет 0 < length < 100.
Примеры

    "abcabc" это действительное слово, потому что "a" появляется дважды, "b" появляется дважды, и "c" появляется дважды.
    "abcabcd" является не действительным словом, потому что "a" появляется дважды, "b" появляется дважды, "c" появляется дважды, но "d" появляется только один раз!
    "123abc!" это действительное слово, потому что все символы появляются только один раз в слове.
"""
import typing
import unittest
from collections import Counter


def validate_word(st: str) -> bool:
    """
    Проверяет, верно ли равенсто одинаковых симвлов в строке.
    """
    return len(set(Counter(st.lower()).values())) == 1


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(validate_word, (
        ("abcabc", True),
        ("Abcabc", True),
        ("AbcabcC", False),
        ("AbcCBa", True),
        ("pippi", False),
        ("abcabcd", False),
        ("?!?!?!", True),
        ("abc123", True),
        ("abc!abc!", True),
        ("abc:abc", False),
    ))
