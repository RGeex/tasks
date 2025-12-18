"""
Найдите пары элементов из двух входных списков, такие что при обмене этих пар суммы элементов в
обоих списках будут равны. Если такой пары не существует, верните пустое множество.
Вход

Два списка целых чисел, list1 и list2с той же длиной.
Выход

Множество кортежей, каждый из которых содержит два элемента ( num_from_list1, num_from_list2 Эти
кортежи представляют собой пары элементов, которые можно поменять местами, чтобы суммы списков
стали равными.
Примеры

fair_swap([1, 1], [2, 2]) ➞ {(1, 2)}

fair_swap([1, 2], [2, 3]) ➞ {(1, 2), (2, 3)}

fair_swap([2], [1, 3]) ➞ {(2, 3)}

fair_swap([2, 3, 4], [11, 4, 1]) ➞ set()

"""
import unittest
from typing import Any, Callable, Tuple, Set, List


def fair_swap(list1: List[int], list2: List[int]) -> Set[Any | Tuple[int, int]]:
    """
    Поиск пар элементов из 2-х списков, при замене котоых сумма списков будет равна.
    """
    return {(a, b) for a in list1 for b in list2 if sum(list1) - a + b == sum(list2) - b + a}


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(fair_swap, (
        (([1, 1], [2, 2]), {(1, 2)}),
        (([1, 2], [2, 3]), {(1, 2), (2, 3)}),
        (([2], [1, 3]), {(2, 3)}),
        (([2, 3, 4], [11, 4, 1]), set()),
        (([0], [1]), set()),
        (([1, 2, 5], [2, 4]), {(5, 4)}),
    ))
