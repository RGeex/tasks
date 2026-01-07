"""
Напишите функцию, которая принимает два аргумента в виде массивов и возвращает новый массив,
заполненный элементами , которые присутствуют в одном из массивов, но не в обоих одновременно.
Каждый элемент должен встречаться в возвращаемом массиве только один раз .

Порядок элементов в результате должен соответствовать порядку элементов в первом массиве,
а затем во втором.
Примеры

[1, 2, 3, 3], [3, 2, 1, 4, 5] --> [4, 5]

["tartar", "blanket", "cinnamon"], ["cinnamon", "blanket", "domino"] --> ["tartar", "domino"]

[77, "ciao"], [78, 42, "ciao"] --> [77, 78, 42]

[1, 2, 3, 3], [3, 2, 1, 4, 5, 4] --> [4,5]

[1, 2, 3] , [3, 3, 2, 1] --> []


"""
import unittest
from typing import Any, Callable, List, Tuple


def hot_singles(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    """
    Находит элементы не повторяющиеся в другом списке и сортирует их по появлению в обоих.
    """
    return sorted(set(arr1).symmetric_difference(set(arr2)), key=(arr1 + arr2).index)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(hot_singles, (
        ((["tartar", "blanket", "domino"], ["blanket"]),["tartar", "domino"]),
        (([77, "basketweave"], [78, 42, "basketweave"]), [77, 78, 42]),
        (([100, 45, "ciao"], [100, 2, 3, 45, 5]), ["ciao", 2, 3, 5]),
        (([10, 200, 30], [10, 20, 3, 4, 5, 5, 5, 200]), [30, 20, 3, 4, 5]),
        (([1, 2, 3, 3], [3, 2, 1, 4, 5, 4]), [4,5]),
    ))
