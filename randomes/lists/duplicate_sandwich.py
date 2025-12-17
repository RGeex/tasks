"""
Задача

В этом ката вам будет дан список, состоящий из уникальных элементов,
за исключением одного, который встречается дважды.

Ваша задача — вывести список всего, что находится между двумя вхождениями этого элемента в списке.
Примеры:

[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
[0, 0] => []
[True, False, True] => [False]
['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']

"""
import unittest
from typing import Any, Callable, Tuple


def duplicate_sandwich(arr: list[Any]) -> list[Any]:
    """
    Выводит список элементов находящихся между 2-мя одинаковыми.
    """
    return next((arr[i:arr.index(n, i)] for i, n in enumerate(arr, 1) if n in arr[i:]), [])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(duplicate_sandwich, (
        ([0, 1, 2, 3, 4, 5, 6, 1, 7, 8], [2, 3, 4, 5, 6]),
        (['None', 'Hello', 'Example', 'hello', 'None', 'Extra'], ['Hello', 'Example', 'hello']),
        ([0, 0], []),
        ([True, False, True], [False]),
        (['e', 'x', 'a', 'm', 'p', 'l', 'e'], ['x', 'a', 'm', 'p', 'l']),
    ))
