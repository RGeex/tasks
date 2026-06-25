"""
Завершите функцию, чтобы найти количество наиболее часто встречающихся элементов массива. Предположим, что на вход подается массив целых чисел. Для пустого массива верните значение функции. 0
Пример

input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 

Наиболее часто встречающееся число в массиве — -1и это происходит 5раз.

"""
import unittest
from typing import Any, Callable, List, Tuple
from collections import Counter


def most_frequent_item_count(collection: List[int]) -> int:
    """
    Определяет макс кол-во повторяющегося элементиа в списке.
    """
    return max([x for _, x in Counter(collection).items()], default=0)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(most_frequent_item_count, (
        ([3, -1, -1], 2),
        ([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3], 5),
        ([], 0),
        ([9], 1),
    ))
