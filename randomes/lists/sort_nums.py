"""
Завершите решение таким образом, чтобы оно сортировало переданный массив чисел.
Если функция передает пустой массив или значение null/nil, она должна вернуть пустой массив.

Например:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []

"""
import unittest
from typing import Any, Callable, List, Tuple


def sort_nums(nums: List[int]) -> List[int]:
    """
    Сортирует список, если он бы передан и не пуст, иначе возвращает пустой список.
    """
    return nums and sorted(nums) or []


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_nums, (
        ([1,2,3,10,5], [1,2,3,5,10]),
        (None, []),
        ([], []),
        ([20,2,10], [2,10,20]),
        ([2,20,10], [2,10,20]),
    ))
