"""
Создайте функцию, которая возвращает сумму двух наименьших положительных чисел,
заданных массивом, состоящим минимум из четырёх положительных целых чисел. Не будут
передаваться числа с плавающей точкой или неположительные целые числа.

Например, когда массив передается как [19, 5, 42, 2, 77], выход должен быть 7.

[10, 343445353, 3453445, 3453545353453]должен вернуться 3453455.
"""
import typing
import unittest


def sum_two_smallest_numbers(numbers: list[int]) -> int:
    """
    Вычисляет сумму 2-х наименьших элементов списка > 0.
    """
    return sum(sorted(filter(lambda x: x > 0, numbers))[:2])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_two_smallest_numbers, (
        ([10, 343445353, 3453445, 3453545353453], 3453455),
        ([5, 8, 12, 18, 22], 13),
        ([7, 15, 12, 18, 22], 19),
        ([25, 42, 12, 18, 22], 30),
    ))
