"""
Напишите функцию, которая выполняет операцию над списком внутри списка:

def grid_map(inp, op)
    # which performs op(element) for all elements of inp

Пример 1:

x = [[1,2,3],
     [4,5,6]]
     
grid_map(x, lambda x: x + 1)
-- returns [[2,3,4],[5,6,7]]

grid_map(x, lambda x: x ** 2)
-- returns [[1,4,9],[16,25,36]]

Пример 2

x = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
grid_map(x, lambda x: x.upper())
-- returns [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]

"""
import unittest
from typing import Any, Callable, List, Tuple


def grid_map(inp: List[List[Any]], op: Callable[[Any], Any]) -> List[List[Any]]:
    """
    применят переданную функцию для применения к вложенным спискам.
    """
    return [list(map(op, x)) for x in inp]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    num_grid = [[1,2,3,4], [5,6,7,8,9], [0,2,4]]
    char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
    test(grid_map, (
        ((num_grid, lambda x: x + 1), [[2,3,4,5], [6,7,8,9,10], [1,3,5]]),
        ((num_grid, lambda x: x * 2), [[2,4,6,8], [10,12,14,16,18], [0,4,8]]),
        ((num_grid, lambda x: x ** 2), [[1,4,9,16],[25,36,49,64,81],[0,4,16]]),
        ((char_grid, lambda x: x.upper()), [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]),
        ((char_grid, lambda x: x.lower()), [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]),
    ))
