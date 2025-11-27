"""
Все началось с обсуждения с другом, который не совсем понял, как установить
значения по умолчанию, но мне показалось, что эта идея достаточно крута для
новичка. Ката: двоичный код ORкаждый совпадающий элемент двух заданных
массивов (или списков, если вы делаете это в Python; векторов в C++) целых
чисел и присвоить полученный массив, объединенный операцией ИЛИ [начинает
звучать как скороговорка, не правда ли?].

Если один массив короче другого, используйте необязательный третий параметр
(по умолчанию 0) к ORнепревзойденные элементы.

Например:

or_arrays([1,2,3],[1,2,3]) == [1,2,3]
or_arrays([1,2,3],[4,5,6]) == [5,7,7]
or_arrays([1,2,3],[1,2]) == [1,2,3]
or_arrays([1,2],[1,2,3]) == [1,2,3]
or_arrays([1,2,3],[1,2,3],3) == [1,2,3]

"""
import typing
import unittest
from itertools import zip_longest as zl


def or_arrays(arr1: list[int], arr2: list[int], data: int = 0) -> list[int]:
    """
    Обяединяет переданные списки.
    """
    return [a | b for a, b in zl(arr1, arr2, fillvalue=data)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(or_arrays, (
        (([1, 2, 3], [1, 2, 3]), [1, 2, 3]),
        (([1, 2, 3], [4, 5, 6]), [5, 7, 7]),
        (([1, 2, 3], [1, 2]), [1, 2, 3]),
        (([1, 0], [1, 2, 3]), [1, 2, 3]),
        (([1, 0, 3], [1, 2, 3], 3), [1, 2, 3]),
    ))
