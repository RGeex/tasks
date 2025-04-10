"""
 семья кукабарр . У меня на заднем дворе живет

Я не вижу их всех, но я их слышу!
Сколько там кукабарр?
Намекать

Секрет подсчета кукабар — внимательно слушать.

    Самцы звучат как HaHaHa...

    Самки звучат как hahaha...

    И они всегда чередуют самцов и самок.

Примеры

    ha= женский => 1
    Ha= мужчина => 1
    Haha= мужчина + женщина => 2
    haHa= женский + мужской => 2
    hahahahaha= женский => 1
    hahahahahaHaHaHa= женский + мужской => 2
    HaHaHahahaHaHa= мужчина + женщина + мужчина => 3

"""
import typing
import unittest
from itertools import groupby


def kooka_counter(st: str) -> str:
    """
    Подсчитывает кол-во пар птиц.
    """
    return len(list(groupby([st[i:i+2] for i in range(0, len(st), 2)])))
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(kooka_counter, (
        ("", 0),
        ("hahahahaha", 1),
        ("hahahahahaHaHaHa", 2),
        ("HaHaHahahaHaHa", 3),
        ("hahahahahahahaHaHa", 2),
    ))
