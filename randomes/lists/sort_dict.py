"""
Словари в Python по своей природе не отсортированы. Что же делать, если нужно отсортировать
содержимое словаря?

Создайте функцию, которая возвращает отсортированный список (key, value)кортежи
(Javascript: массивы из 2 элементов).

Список должен быть отсортирован по valueи отсортировать от наибольшего к наименьшему.
Примеры

sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
"""
import unittest
from typing import Any, Callable, Tuple


def sort_dict(dct: dict[str | int, int]) -> list[tuple[str | int, int]]:
    """
    Сортирует словарь.
    """
    return sorted(dct.items(), key=lambda x: x[1], reverse=True)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_dict, (
        ({1: 3, 2: 2, 3: 1}, [(1, 3), (2, 2), (3, 1)]),
        ({3: 1, 2: 2, 1: 3}, [(1, 3), (2, 2), (3, 1)]),
        ({1: 2, 2: 4, 3: 6}, [(3, 6), (2, 4), (1, 2)]),
        ({1: 5, 3: 10, 2: 2, 6: 3, 8: 8}, [(3, 10), (8, 8), (1, 5), (6, 3), (2, 2)]),
        ({'a': 6, 'b': 2, 'c': 4}, [('a', 6), ('c', 4), ('b', 2)]),
    ))
