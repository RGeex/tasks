"""
Дан несортированный массив целых чисел. Найдите наименьшее число в массиве,
наибольшее число в массиве и наименьшее число между двумя границами массива,
которое не входит в массив.

Например, если задан массив [-1, 4, 5, -23, 24], наименьшее число равно -23,
наибольшее — 24, а наименьшее число между границами массива — -22.
Можно предположить, что входные данные корректно сформированы.

Ваше решение должно возвращать массив[smallest, minimumAbsent, largest]

Целое smallestчисло должно быть целым числом из массива с наименьшим значением.

Целое largestчисло должно быть целым числом из массива с наибольшим значением.

Это minimumAbsentнаименьшее число между наибольшим и наименьшим числом,
которого нет в массиве.

minMinMax([-1, 4, 5, -23, 24]); //[-23, -22, 24]
minMinMax([1, 3, -3, -2, 8, -1]); //[-3, 0, 8]
minMinMax([2, -4, 8, -5, 9, 7]); //[-5, -3,9]
"""
import typing
import unittest


def min_min_max(arr: list[int]) -> list[int]:
    """
    Из переданного списка создается новый, согласно условию.
    """
    return sorted([*(x := sorted(arr)[::len(arr) - 1]), next(n for n in range(*x) if n not in arr)])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(min_min_max, (
        ([-1, 4, 5, -23, 24], [-23, -22, 24]),
        ([1, 3, -3, -2, 8, -1], [-3, 0, 8]),
        ([2, -4, 8, -5, 9, 7], [-5, -3, 9]),
    ))
