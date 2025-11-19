"""
Напишите функцию, которая сглаживает множество Arrayобъектов Array в плоский
объект Array. Функция должна выполнять только один уровень сглаживания.

flatten([1,2,3])  ==> [1,2,3]
flatten([[1,2,3],["a","b","c"],[1,2,3]])  ==> [1,2,3,"a","b","c",1,2,3]
flatten([[[1,2,3]]])  ==> [[1,2,3]]
"""
import typing
import unittest


def flatten(lst: list[int | str | list]) -> list[int | str | list]:
    """
    Распаковывает элемент списка если он является списком.
    """
    return [a for b in lst for a in [[b], b][isinstance(b, list)]]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(flatten, (
        ([], []),
        ([1,2,3], [1,2,3]),
        ([[1,2,3], ["a", "b", "c"], [1,2,3]], [1,2,3,"a","b","c",1,2,3]),
        ([[1,2,3], ["a", "b", "c"], [1,2,3], "a"], [1,2,3,"a","b","c",1,2,3,"a"]),
        ([[3,4,5],[[9,9,9]],["a,b,c"]], [3,4,5,[9,9,9],"a,b,c"]),
        ([[[3],[4],[5]],[9],[9],[8],[[1,2,3]]], [[3],[4],[5],9,9,8,[1,2,3]])
    ))
