"""
В этой кате вам будет предоставлена ​​серия раз, когда звучит тревога. Ваша задача будет
заключаться в том, чтобы определить максимальный интервал времени между тревогами.
Каждая тревога начинает звонить в начале соответствующей минуты и звонит ровно в
течение одной минуты. Время в массиве не в хронологическом порядке. Игнорировать
дубликаты времен, если таковые имеются.

For example:
solve(["14:51"]) = "23:59". If the alarm sounds now, it will not sound for another 23
hours and 59 minutes.
solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will
not sound is 11 hours and 40 minutes.

Во втором примере звучит тревога 4 раз в день.
"""
import typing
import unittest
from datetime import datetime, timedelta


def max_interval_alarm(arr: list[str]) -> str:
    """
    Поиск максимальной разницы во времени между звонками будильника.
    """
    arr = sorted([datetime.strptime(x, '%H:%M') for x in set(arr)])
    return max(f'{str(x - arr[i] - timedelta(minutes=1)).split(", ")[-1][:-3]:0>5}' for i, x in enumerate(arr, -1)) if 1 < len(arr) else '23:59'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_interval_alarm, (
        (["14:51"], "23:59"),
        (["23:00", "04:22", "18:05", "06:24"], "11:40"),
        (["21:14", "15:34", "14:51", "06:25", "15:30"], "09:10"),
    ))
