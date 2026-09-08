"""
Для целого числа kпереставьте все элементы заданного массива таким образом, чтобы:

Все элементы, которые меньше определенного значения, k располагаются перед элементами, которые не меньше определенного значения k;
все элементы, которые меньше определенного значения, k сохраняют свой порядок относительно друг друга;
все элементы, которые не меньше k определенного значения, сохраняют свой порядок относительно друг друга.

Для значений k = 6и elements = [6, 4, 10, 10, 6], результат должен быть splitByValue(k, elements) = [4, 6, 10, 10, 6].

При k= 5 и elements = [1, 3, 5, 7, 6, 4, 2], на выходе должно быть splitByValue(k, elements) = [1, 3, 4, 2, 5, 7, 6].
"""
import unittest
from typing import Any, Callable, List, Tuple


def split_by_value(k: int, elements: List[int]) -> List[int]:
    """
    Сортирует элементы.
    """
    res = [[], []]
    for n in elements:
        res[n >= k].append(n)
    return [b for a in res for b in a]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(split_by_value, (
        ((5, [1, 3, 5, 7, 6, 4, 2]), [1, 3, 4, 2, 5, 7, 6]),
        ((0, [5, 2, 7, 3, 2]),[5, 2, 7, 3, 2]),
        ((6, [6, 4, 10, 10, 6]),[4, 6, 10, 10, 6]),
    ))
