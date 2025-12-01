"""
Напишите функцию describeList, которая возвращает «пустой», если список пуст,
или «синглтон», если он содержит только один элемент, или «длиннее», если их больше.
"""
import typing
import unittest


def describe_list(lst: list[int]) -> str:
    """
    Определяет длину переданного списка.
    """
    return {0: "empty", 1: "singleton"}.get(len(lst), "longer")


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(describe_list, (
        ([], "empty"),
        ([1], "singleton"),
        ([1, 2, 5, 4], "longer"),
    ))
