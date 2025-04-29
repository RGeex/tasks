"""
Напишите функцию, которая получает две строки в качестве параметра.
Эти строки имеют следующий формат даты: YYYY/MM/DD.
Ваша задача:взять yearsи вычислить разницу между ними.
Примеры:

'1997/10/10' and '2015/10/10' -> 2015 - 1997 = returns 18
'2015/10/10' and '1997/10/10' -> 2015 - 1997 = returns 18

На этом уровне вам не нужно проверять месяцы и дни для расчета разницы.
"""
import typing
import unittest
from operator import sub


def how_many_years(date1: str, date2: str) -> int:
    """
    Вычисляет разницу лет между двумя датами в виде строки.
    """
    return next(abs(sub(*map(int, x))) for x in zip(*[x.split('/') for x in (date1, date2)]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(how_many_years, (
        (('1997/10/10', '2015/10/10'), 18),
        (('1990/10/10', '2015/10/10'), 25),
        (('2015/10/10', '1990/10/10'), 25),
        (('1992/10/24', '2015/10/24'), 23),
        (('2018/10/10', '2000/10/10'), 18),
    ))
