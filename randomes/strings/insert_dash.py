"""
Напишите функцию, которая занимает целое число num ( num >= 0) и вставляют тире ( '-') между каждыми двумя нечетными цифрами в num.
Примеры

454793 ---> "4547-9-3"
     0 ---> "0"
     1 ---> "1"
13579  ---> "1-3-5-7-9"
 86420 ---> "86420"
"""
import typing
import unittest


def insert_dash(num: int) -> str:
    """
    Разделяет нечетные цифры стоящие рядом.
    """
    res, prew = '', 0
    for n in str(num):
        res, prew = res + ['', '-'][int(n) % 2 and prew % 2] + n, int(n)
    return res


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(insert_dash, (
        (454793, '4547-9-3'),
        (123456, '123456'),
        (1003567, '1003-567'),
        (24680, '24680'),
        (13579, '1-3-5-7-9'),
    ))
