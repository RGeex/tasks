"""
Задача

Напишите функцию nico/ nico() который принимает два параметра:

    key/ $key - строка состоит из уникальных букв и цифр
    message/ $message - строка для кодирования

и кодирует message используя key.

Сначала создайте цифровой ключ на основе предоставленного key назначая каждой букве позицию,
в которой она находится после установки букв из key в алфавитном порядке.

Например, для ключа crazy мы получим 23154 из-за acryz (сортировка букв по ключу).
Давайте закодируем secretinformation используя наш crazy ключ.

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n

После использования ключа:

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n

Примеры

nico("crazy", "secretinformation") => "cseerntiofarmit on  "
nico("abc", "abcd") => "abcd  "
nico("ba", "1234567890") => "2143658709"
nico("key", "key") => "eky"
"""
import typing
import unittest
from math import ceil
from operator import truediv


def nico1(key: str, message: str) -> str:
    """
    Шифрует строку по заданному ключу.
    """
    k = {v: k for k, (v, _) in enumerate(sorted(enumerate(key), key=lambda x: x[1]))}
    res = ['_'] * ((x := ceil(truediv(*map(len, (message, key))))) * (c := len(key)))
    for n in range(x):
        for i, x in enumerate(f'{message[n * c:n * c + c]:<{c}}'):
            res[k[i] + c * n] = x
    return ''.join(res)


def nico2(key: str, msg: str) -> str:
    """
    Шифрует строку по заданному ключу.
    """
    x = (m := len(msg)) // (k := len(key)) + bool(m % k)
    return ''.join([''.join([x for _, x in sorted(zip(key, f'{msg[n * k:n * k + k]:<{k}}'))]) for n in range(x)])


def test(funcs: tuple[typing.Callable], data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    for n, func in enumerate(funcs, 1):
        funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
        suite = unittest.TestLoader().loadTestsFromTestCase(
            type(f'Tests_{n}', (unittest.TestCase,), funcs))

        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test((nico1, nico2), (
        (("crazy", "secretinformation"), "cseerntiofarmit on  "),
        (("abc", "abcd"), "abcd  "),
        (("ba", "1234567890"), "2143658709"),
        (("a", "message"), "message"),
        (("key", "key"), "eky"),
        (("abcdefgh", "abcd"), "abcd    "),
    ))
