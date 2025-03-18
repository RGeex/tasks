"""
Создайте функцию, которая принимает одну произвольную строку в качестве аргумента и возвращает
строку длиной 26.

Цель состоит в том, чтобы установить каждый из 26 символов выходной строки в одно из следующих
значений: '1' или '0'на основе того, присутствует ли во входных данных N-я буква алфавита
(независимо от ее регистра).

Так что если 'a'или 'A'появляется в любом месте входной строки (любое количество раз), установите
первый символ выходной строки в '1', в противном случае '0'. если 'b' или 'B'появляется в строке,
установите второй символ на '1'и так далее для остальной части алфавита.

Например:

"a   **&  cZ"  =>  "10100000000000000000000001"

"aaaaaaa79345675"  =>  "10000000000000000000000000"

"&%#*"  =>  "00000000000000000000000000"
"""
import typing
import unittest
from string import ascii_lowercase


def change(st: str) -> str:
    """
    Создает строку из 26 символов 0, заменяя на 1 если в заданной строке присутствует
    буква алфавита соответствующая порядковому номеру.
    """
    return ''.join(['01'[x in st.lower()] for x in ascii_lowercase])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(change, (
        ("a **&  bZ", "11000000000000000000000001"),
        ('Abc e  $$  z', "11101000000000000000000001"),
        ("!!a$%&RgTT", "10000010000000000101000000"),
        ("", "00000000000000000000000000"),
        ("abcdefghijklmnopqrstuvwxyz", "11111111111111111111111111"),
        ("aaaaaaaaaaa", "10000000000000000000000000"),
        ("&%&%/$%$%$%$%GYtf67fg34678hgfdyd", "00010111000000000001000010"),
    ))
