"""
Вам будет передан массив объектов ( list) — вы должны отсортировать их в
порядке убывания на основе значения указанного свойства ( sortBy).

Пример
При сортировке по "a"это:

[
  {"a": 1, "b": 3},
  {"a": 3, "b": 2},
  {"a": 2, "b": 40},
  {"a": 4, "b": 12}
]
должен вернуть:

[
  {"a": 4, "b": 12},
  {"a": 3, "b": 2},
  {"a": 2, "b": 40},
  {"a": 1, "b": 3}
]
Значения всегда будут числами, а свойства всегда будут существовать.
"""
import typing
import unittest


def sort_list(sort_by: str, lst: list) -> list:
    """
    Сортирует список по переданному ключу.
    """
    return sorted(lst, key=lambda x: x.get(sort_by), reverse=True)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_list, (
        (("x", []),[]),
        (("b",
            [
                {"a": 2, "b": 2},
                {"a": 3, "b": 40},
                {"a": 1, "b": 12}
            ]), [
                {"a": 3, "b": 40},
                {"a": 1, "b": 12},
                {"a": 2, "b": 2}
            ]),
        (("a",
            [
                {"a": 4, "b": 3},
                {"a": 2, "b": 2},
                {"a": 3, "b": 40},
                {"a": 1, "b": 12}
            ]), [
                {"a": 4, "b": 3},
                {"a": 3, "b": 40},
                {"a": 2, "b": 2},
                {"a": 1, "b": 12}
            ]),
    ))
