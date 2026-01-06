"""
Реализуйте функцию для вычисления суммы числовых значений во вложенном списке. Например:

sum_nested([1, [2, [3, [4]]]]) -> 10

"""
import unittest
from typing import Any, Callable, List, Tuple


def sum_nested(lst: List[Any]) -> int:
    """
    Подсчитывает сумму чисел в списке любой вложенности.
    """
    return sum(sum_nested(x) if isinstance(x, list) else x for x in lst)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_nested, (
        ([1], 1),
        ([1, 2, 3, 4], 10),
        (list(range(11)), 55),
        ([], 0),
        ([[1], []], 1),
        ([[1, 2, 3, 4]], 10),
        ([[], []], 0),
        ([1, [1], [[1]], [[[1]]]], 4),
        ([1, [1], [1, [1]], [1, [1], [1, [1]]]], 8),
        ([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []], 0),
    ))
