"""
Написать функцию lastкоторый принимает список и возвращает последний элемент в списке.

Если список пуст:

В языках, которые имеют встроенный option или resultтип (например, OCaml или Haskell), возвращает пустой option

В языках, где нет пустого варианта, просто верните None

"""
import typing
import unittest


def last(lst: list[typing.Any]) -> typing.Any:
    """
    Возвращает последний элемент в списке, если список не пуст, иначе None.
    """
    return lst[-1] if lst else None


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(last, (
        ([1, 2, 3], 3),
        ([], None),
    ))
