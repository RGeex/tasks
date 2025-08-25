"""
Учитывая код в виде массива строк, вернуть одну строку, представляющую
значение кода, найденное путем его преобразования.

Массив будет иметь длину не менее 1, а все составляющие его строки будут
иметь одинаковую длину n. Каждая строка состоит только из строчных букв
и пробелов.

Каждый символ выходной строки представляет собой среднее арифметическое
соответствующих символов входных строк. Это означает, что первый символ
выходной строки представляет собой среднее арифметическое первых символов
всех входных строк, второй символ выходной строки представляет собой среднее
арифметическое вторых символов всех входных строк и т. д. Если среднее
значение не является целым числом, округлите его в меньшую сторону.

Для каждого символа с индексом n входной строки μ = σ/L, где μ представляет
собой алфавитный индекс n-го символа выходной строки, σ представляет собой
сумму n-х символов всех строк, а L представляет собой длину входного массива строк.

Пробелам присваивается значение 0. Буквам присваивается значение, равное их
алфавитному индексу. a = 1, b = 2, c = 3 и так далее.

Пример

String s1 = "u lk zxuq hfk as fouh";
String s2 = "y l  zpuv  xe at sicd";
String s3 = "welvayfuqbfpeaauaqcrc";
              
String sμ = "walk your dog at nine";

index 0: 'u' = 21, 'y' = 25, 'w' = '23', μ = 23 = 'w'
index 1: ' ' = 0,  ' ' = 0,  'e' = 5,    μ = 1.667 = 'a'
"""
import typing
import unittest
from string import ascii_lowercase as abc


def decipher(code: list[str]) -> str:
    """
    Из заданных строк получает среднее значение.
    """
    return ''.join(f' {abc}'[sum(map(f' {abc}'.index, x)) // len(code)] for x in zip(*code))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(decipher, (
        (["u lk zxuq hfk as fouh","y l  zpuv  xe at sicd","welvayfuqbfpeaauaqcrc"], "walk your dog at nine"),
        (["hello world"], "hello world"),
        (["","","","",""], ""),
        (["a  "," b ","  c","   ","   "], "   "),
        (["foreman pig", "foreman pig"], "foreman pig"),
    ))
