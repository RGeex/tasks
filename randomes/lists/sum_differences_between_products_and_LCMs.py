"""
В этом ката вам нужно создать функцию, которая принимает двумерный
массив/список пар неотрицательных целых чисел и возвращает сумму всех
«экономий», которые вы можете получить, получив НОК каждой пары чисел
по сравнению с их простым произведением.

Например, если вам дано:

[[15,18], [4,5], [12,60]]
Их продукт будет следующим:

[270, 20, 720]
В то время как их соответствующие НОК будут:

[90, 20, 60]
Таким образом, результат должен быть:

(270-90)+(20-20)+(720-60)==840
Это ката, которое я сделал, помимо прочего, для того, чтобы некоторые из
моих учеников могли ознакомиться с алгоритмом Евклида , действительно
полезный инструмент, который можно носить на поясе ;)
"""
import typing
import unittest
from math import gcd


def sum_differences_between_products_and_LCMs(pairs: list[list[int]]) -> int:
    """
    Вычисляет сумму экономий.
    """
    return sum(a * b - a * b // gcd(a, b) for a, b in pairs if b)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_differences_between_products_and_LCMs, (
        ([[15,18], [4,5], [12,60]],840),
        ([[1,1], [0,0], [13,91]],1092),
        ([[15,7], [4,5], [19,60]],0),
        ([[20,50], [10,10], [50,20]],1890),
        ([],0),
    ))
