"""
Вам дана сетка символов размером n на n (квадратная), например:

[['m', 'y', 'e'], 
 ['x', 'a', 'm'], 
 ['p', 'l', 'e']]

Вам также предоставляется список целых чисел в качестве входных данных, например:

[1, 3, 5, 8]

Если рассматривать индексы как: вам нужно найти символы в этих индексах сетки.

[[1, 2, 3], 
 [4, 5, 6], 
 [7, 8, 9]]

Помните, что индексы начинаются с единицы, а не с нуля.

Затем вы получите строку примерно такого вида:

"meal"

Все введенные данные будут действительными.

"""
import unittest
from typing import Any, Callable, List, Tuple


def grid_index(grid: List[List[str]], indexes: List[int]) -> str:
    """
    Вытаскивает символы из квадратной матрицы по их порядковому номеру.
    """
    data = dict([(i, x) for i, x in enumerate([b for a in grid for b in a], 1) if i in indexes])
    return ''.join(data[x] for x in indexes)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(grid_index, (
        (([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9]), 'myexample'),
        (([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6]), 'mam'),
        (([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8]), 'mepl'),
        (([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']], [5, 7, 9, 3, 6, 6, 8, 8, 16, 13]), 'ooelccddrr'),
    ))
