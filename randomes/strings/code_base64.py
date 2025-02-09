"""
Расширить объект String (JS) или создать функцию (Python, C#), которая преобразует значение строки
в Base64 и обратно, используя набор символов ASCII (UTF-8 для C#).
Пример (input -> output):

'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'

Вы можете узнать больше о кодировании и декодировании . BASE64

ПРИМЕЧАНИЕ. В этой Kata используется неэтипендическая версия ("=" не добавляется до конца).
"""
import base64
import typing
import unittest
from functools import reduce


def to_base_64(st: str) -> str:
    """
    Кодирование строки в base64.
    """
    return base64.b64encode(st.encode('utf-8')).decode('utf-8').replace('=', '')


def from_base_64(st: str) -> str:
    """
    Декодирование строки из base64.
    """
    return base64.b64decode((st + '=' * (4 - len(st) % 4)).encode('utf-8')).decode('utf-8')


def test(funcs: tuple[typing.Callable], data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = [{f'test_{func.__name__}_{i}': test_func(func, *args[::n or -1]) for i, args in enumerate(data, 1)} for n, func in enumerate(funcs)]
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), reduce(lambda a, b: a | b, funcs)))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test((from_base_64, to_base_64), (
        ["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
        ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
        ["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
        ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
        ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
        ["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
        ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
        ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
        ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]
    ))
