"""
Необходимо поменять местами начало и конец указанного массива:

Первая половина массива (голова) перемещается в конец, вторая половина (хвост) — в начало.
Средний элемент, если он существует, остается на том же месте.

Возвращает новый массив. Не изменяет входные данные.

Например:

[ 1, 2, 3, 4, 5 ]   =>  [ 4, 5, 3, 1, 2 ]
 \----/   \----/         
  head     tail 

[ -1, 2 ]  => [ 2, -1 ] 
[ 1, 2, -3, 4, 5, 6, -7, 8 ]   =>  [ 5, 6, -7, 8, 1, 2, -3, 4 ]  
"""
import unittest
from typing import Any, Callable, List, Tuple


def swap_head_tail(arr: List[int]) -> List[int]:
    """
    Меняет местами начало и конец списка.
    """
    a, b = divmod(len(arr), 2)
    return arr[a + b:] + arr[a:a + b] + arr[:a]


def swap_head_tail_2(arr: List[int]) -> List[int]:
    """
    Меняет местами начало и конец списка.
    """
    x = len(arr) // 2
    return arr[-x:] + arr[x:-x] + arr[:x]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(swap_head_tail, (
        ([1, 2, 3, 4, 5], [4, 5, 3, 1, 2]),
        ([-1, 2], [2, -1]),
        ([1, 2, -3, 4, 5, 6, -7, 8], [5, 6, -7, 8, 1, 2, -3, 4]),
        ([1], [1]),
    ))
    test(swap_head_tail_2, (
        ([1, 2, 3, 4, 5], [4, 5, 3, 1, 2]),
        ([-1, 2], [2, -1]),
        ([1, 2, -3, 4, 5, 6, -7, 8], [5, 6, -7, 8, 1, 2, -3, 4]),
        ([1], [1]),
    ))
