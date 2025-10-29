"""
Мера Стэнтона массива определяется следующим образом:
Пусть n — число раз, которое значение 1появляется в массиве.
Мера Стэнтона — это количество раз, которое n встречается в массиве.

Задача
Напишите функцию, которая принимает целочисленный массив и возвращает его меру Стэнтона.

Примеры
Для [1, 4, 3, 2, 1, 2, 3, 2]:
1появляется 2 раза → 2встречается 3 раза → мера Стэнтона = 3 .

Для [1, 4, 1, 2, 11, 2, 3, 1]:
1появляется 3 раза → 3появляется 1 раз → мера Стэнтона = 1 .
"""
import typing
import unittest


def stanton_measure(arr: list[int]) -> int:
    """
    Определяет меру стентона.
    """
    return arr.count(arr.count(1))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(stanton_measure, (
        ([1, 4, 3, 2, 1, 2, 3, 2], 3),
    ))
