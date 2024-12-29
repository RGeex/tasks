"""
Напишите класс, который при получении строки будет возвращать строку в верхнем регистре,
в которой каждая буква сдвинута вперед в алфавите на любое количество мест, на которые
был инициализирован шифр.

Например:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'

Если что-то в строке отсутствует в алфавите (например, знаки препинания, пробелы), просто
оставьте все как есть.
Сдвиг всегда будет находиться в диапазоне [1, 26].
"""
import typing


class CaesarCipher(object):
    """Кодирование и декодирование строки смещением с заданным шагом."""

    def __init__(self, shift):
        self.shift = shift

    @staticmethod
    def convert(s: str, n: int) -> str:
        """Кодирование строки в заданном направлении."""
        return ''.join([chr((ord(x) - 65 + n) % 26 + 65) if x.isalpha() else x for x in s.upper()])

    def encode(self, st: str) -> str:
        """Кодирование строки в прямом направлении."""
        return CaesarCipher.convert(st, self.shift)

    def decode(self, st: str) -> str:
        """Кодирование строки в обратном направлении."""
        return CaesarCipher.convert(st, -self.shift)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    cipher = CaesarCipher(5)
    test(cipher.encode, (('Codewars', 'HTIJBFWX'),))
    test(cipher.decode, (('HTIJBFWX', 'CODEWARS'),))
