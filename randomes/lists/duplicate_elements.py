"""
Даны два массива целых чисел mи n. Проверьте, содержат ли они хотя бы один одинаковый элемент. Верните значение, true если содержат; false если нет.

Ваш код должен обрабатывать любое значение в диапазоне 32-битного целого числа и должен быть способен обрабатывать как пустой массив
(что является falseрезультатом, поскольку в нем нет повторяющихся элементов).
"""
import unittest
from typing import Any, Callable, List, Tuple


def duplicate_elements(m: List[int], n: List[int]) -> bool:
    """
    Проверяет, есть ли общие элементы в 2-х списках.
    """
    return bool(set(m) & set(n))


def duplicate_elements_2(m: List[int], n: List[int]) -> bool:
    """
    Проверяет, есть ли общие элементы в 2-х списках.
    """
    return not set(m).isdisjoint(n)


def duplicate_elements_3(m: List[int], n: List[int]) -> bool:
    """
    Проверяет, есть ли общие элементы в 2-х списках.
    """
    return any(x in n for x in m)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(duplicate_elements, (
        (([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True),
        (([9, 8, 7], [8, 1, 3]), True),
        (([-2, -4, -6, -8], [-2, -3, -5, -7]), True),
        (([-9, -8, -7], [-8, -1, -3]), True),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8]), False),
        (([9, 8, 7], [6, 5, 4]), False),
        (([], [9, 8, 7, 6, 5]), False),
        (([9, 8, 7, 6, 5], []), False),
        (([], []), False),
    ))
    test(duplicate_elements_2, (
        (([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True),
        (([9, 8, 7], [8, 1, 3]), True),
        (([-2, -4, -6, -8], [-2, -3, -5, -7]), True),
        (([-9, -8, -7], [-8, -1, -3]), True),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8]), False),
        (([9, 8, 7], [6, 5, 4]), False),
        (([], [9, 8, 7, 6, 5]), False),
        (([9, 8, 7, 6, 5], []), False),
        (([], []), False),
    ))
    test(duplicate_elements_3, (
        (([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True),
        (([9, 8, 7], [8, 1, 3]), True),
        (([-2, -4, -6, -8], [-2, -3, -5, -7]), True),
        (([-9, -8, -7], [-8, -1, -3]), True),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8]), False),
        (([9, 8, 7], [6, 5, 4]), False),
        (([], [9, 8, 7, 6, 5]), False),
        (([9, 8, 7, 6, 5], []), False),
        (([], []), False),
    ))
