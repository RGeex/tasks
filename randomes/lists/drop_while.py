"""
Ещё один важный приём для функционального программиста. У вас есть последовательность значений и
некоторый предикат для этих значений. Вы хотите удалить самый длинный префикс элементов таким образом,
чтобы предикат был истинным для каждого элемента. Назовём это функцией dropWhile. Она принимает два
аргумента. Первый — это последовательность значений, а второй — функция предиката. Функция не
изменяет значение исходной последовательности.

def isEven(num):
  return num % 2 == 0

arr = [2,4,6,8,1,2,5,4,3,2]

dropWhile(arr, isEven) == [1,2,5,4,3,2] # True

Ваша задача — реализовать функцию dropWhile. Если у вас есть готовая функция span , это можно
сделать одной строкой кода! В качестве альтернативы, если у вас есть функция takeWhile , то в
сочетании с функцией dropWhile вы можете реализовать функцию span в одной строке. В этом и
заключается прелесть функционального программирования: существует множество полезных функций,
многие из которых можно реализовать через другие функции.


"""
import unittest
from typing import Any, Callable, List, Tuple


def drop_while(arr: List[int], pred: Callable[[int], bool]) -> List[int]:
    """
    Удаляет самый длинный префикс элементов.
    """
    return next((arr[i:] for i, x in enumerate(arr) if not pred(x)), [])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    def is_even(n): return not n % 2
    def is_odd(n): return n % 2
    test(drop_while, (
        (([2, 6, 4, 10, 1, 5, 4, 3], is_even), [1, 5, 4, 3]),
        (([2, 100, 1000, 10000, 10000, 5, 3, 4, 6], is_even), [5, 3, 4, 6]),
        (([998, 996, 12, -1000, 200, 0, 1, 1, 1], is_even), [1, 1, 1]),
        (([1, 4, 2, 3, 5, 4, 5, 6, 7], is_even), [1, 4, 2, 3, 5, 4, 5, 6, 7]),
        (([2, 4, 10, 100, 64, 78, 92], is_even), []),
        (([1, 2, 3, 4, 5], is_odd), [2, 3, 4, 5]),
        (([1, 5, 111, 1111, 1111, 2, 4, 6, 4, 5], is_odd), [2, 4, 6, 4, 5]),
        (([-1, -5, 127, 86, 902, 2, 1], is_odd), [86, 902, 2, 1]),
        (([2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0], is_odd), [2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0]),
        (([1, 3, 5, 7, 9, 111], is_odd), []),
    ))
