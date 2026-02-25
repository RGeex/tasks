"""
Определите метод/функцию, которая удаляет из заданного массива целых чисел все значения,
содержащиеся во втором массиве.
Примеры (вход -> выход):

* [1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]
* [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2] -> [5, 6, 7, 8]
* [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3] -> [8, 7, 6, 5, 1]

Наслаждайся этим!!

"""
import unittest
from typing import Any, Callable, List, Tuple


def remove_(integer_list: List[int], values_list: List[int]) -> List[int]:
    """
    Оставляет данные первого списка, кроме содержащихся во втором.
    """
    return [n for n in integer_list if n not in values_list]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_, (
        (([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]), [2, 2, 4]),
        (([1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2]), [5, 6, 7, 8]),
        (([8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3]), [8, 7, 6, 5, 1]),
        (([4, 4, 2, 3], [2, 2, 4, 3]), []),
        (([], [2, 2, 4, 3]), []),
    ))
