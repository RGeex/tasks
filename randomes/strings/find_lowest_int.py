"""
У нас есть два последовательных целых числа k1k_1к 1 и k2k_2к 2 
где k2=k1+1k_2 = k_1 + 1к 2 = к 1 + 1 .

Нам нужно вычислить наименьшее строго положительное целое число n,
такой что: ценности n⋅k1n \cdot k_1н ⋅ к 1 и n⋅k2n \cdot k_2н
к 2 имеют те же цифры, но в разном порядке.

Пример №1:

k1 = 100
k2 = 101
n = 8919
#Because 8919 * 100 = 891900
and      8919 * 101 = 900819

Пример №2:

k1 = 325
k2 = 326
n = 477
#Because 477 * 325 = 155025
and      477 * 326 = 155502

Ваша задача — подготовить функцию, которая будет получать значение
k и выводит значение n.

Приведенные выше примеры будут следующими:

Input: 100 --> Return: 8919
Input: 325 --> Return:  477

Особенности случайных тестов

10 < k < 10.000.000.000.000.000 (For Python, Ruby and Haskell)
10 < k < 1.000.000.000  (For Javascript and D 1e9)
"""
import typing
import unittest
from operator import eq


def find_lowest_int(k: int) -> int:
    """
    Поиск числа N.
    """
    n = 1
    while not eq(*[sorted(str((k + i) * n)) for i in range(2)]):
        n += 1
    return n


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_lowest_int, (
        (325, 477),
        (599, 2394),
        (855,  999),
        (1, 125874),
        (100, 8919),
        (1000, 89919),
        (10000, 899919),
    ))
