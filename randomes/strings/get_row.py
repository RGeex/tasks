"""
Задача

Реализуйте функцию, которая принимает число Nи возвращает N'-я строка
последовательности ниже. Если аргумент больше количества строк в
последовательности, то начинаем сначала, например, со строки 27
то же самое, что и строка 1.
Последовательность

1:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
2:  BBCDEFGHIJKLMNOPQRSTUVWXYZ
3:  CCCDEFGHIJKLMNOPQRSTUVWXYZ
4:  DDDDEFGHIJKLMNOPQRSTUVWXYZ
5:  EEEEEFGHIJKLMNOPQRSTUVWXYZ
6:  FFFFFFGHIJKLMNOPQRSTUVWXYZ
7:  GGGGGGGHIJKLMNOPQRSTUVWXYZ
8:  HHHHHHHHIJKLMNOPQRSTUVWXYZ
9:  IIIIIIIIIJKLMNOPQRSTUVWXYZ
10: JJJJJJJJJJKLMNOPQRSTUVWXYZ
11: KKKKKKKKKKKLMNOPQRSTUVWXYZ
12: LLLLLLLLLLLLMNOPQRSTUVWXYZ
13: MMMMMMMMMMMMMNOPQRSTUVWXYZ
14: NNNNNNNNNNNNNNOPQRSTUVWXYZ
15: OOOOOOOOOOOOOOOPQRSTUVWXYZ
16: PPPPPPPPPPPPPPPPQRSTUVWXYZ
17: QQQQQQQQQQQQQQQQQRSTUVWXYZ
18: RRRRRRRRRRRRRRRRRRSTUVWXYZ
19: SSSSSSSSSSSSSSSSSSSTUVWXYZ
20: TTTTTTTTTTTTTTTTTTTTUVWXYZ
21: UUUUUUUUUUUUUUUUUUUUUVWXYZ
22: VVVVVVVVVVVVVVVVVVVVVVWXYZ
23: WWWWWWWWWWWWWWWWWWWWWWWXYZ
24: XXXXXXXXXXXXXXXXXXXXXXXXYZ
25: YYYYYYYYYYYYYYYYYYYYYYYYYZ
26: ZZZZZZZZZZZZZZZZZZZZZZZZZZ
"""
import typing
import unittest
from string import ascii_uppercase as abc


def get_row(n: int) -> str:
    """
    Создает последовательность алфавита с заданного символа.
    """
    return f'{abc[n % 26 - 1:]:{abc[n % 26 - 1]}>26}'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_row, (
        (  1, "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ),
        ( 26, "ZZZZZZZZZZZZZZZZZZZZZZZZZZ" ),
        ( 15, "OOOOOOOOOOOOOOOPQRSTUVWXYZ" ),
        ( 27, "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
    ))

