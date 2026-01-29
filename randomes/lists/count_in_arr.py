"""
Даны два массива строк. Верните количество раз,
которое каждая строка из второго массива встречается в первом массиве.
Пример

array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
array2 = ['abc', 'cde', 'uap']

Сколько раз встречаются элементы в array2появляются в array1?

    'abc'появляется дважды в первом массиве (2)
    'cde'появляется только один раз (1)
    'uap'не появляется в первом массиве (0)

Поэтому, solve(array1, array2) = [2, 1, 0]

Удачи! 
"""
import unittest
from typing import Any, Callable, List, Tuple
from collections import Counter


def count_in_arr(a: List[str], b: List[str]) -> List[int]:
    """
    Определяет кол-во раз, встречающихся строок из списка 2 в списке 1.
    """
    x = Counter(a)
    return [x.get(s, 0) for s in b]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_in_arr, (
        ((['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']), [2, 1, 0]),
        ((['abc', 'xyz', 'abc', 'xyz', 'cde'], ['abc', 'cde', 'xyz']), [2, 1, 2]),
        ((['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1]),
    ))
