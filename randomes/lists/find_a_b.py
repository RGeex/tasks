"""
Задача:

Предоставят вам числовой массив numbersи ряд c.

Найдите пару чисел (мы назвали их числом a и числом b) в массиве. numbersПусть a*b=c, формат результата — массив. [a,b]

Массив numbersЭто отсортированный массив, диапазон значений: -100...100

В результате получится первая пара чисел, например: findAB([1,2,3,4,5,6],6)должен вернуться [1,6], вместо [2,3]

Дополнительные примеры смотрите в разделе тестовых случаев. 

"""
import unittest
from typing import Any, Callable, List, Tuple


def find_a_b(numbers: List[int], c: int) -> List[int] | None:
    """
    Поисп ближайших пар чисел удовлетворяющих условию.
    """
    return next(([a, b] for i, a in enumerate(numbers[:-1], 1) for b in numbers[i:] if a * b == c), None)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_a_b, (
        (([1, 2, 3], 3), [1, 3]),
        (([1, 2, 3], 6), [2, 3]),
        (([1, 2, 3], 7), None),
        (([1, 2, 3, 6], 6), [1, 6]),
        (([1, 2, 3, 4, 5, 6], 15), [3, 5]),
        (([0, 0, 2], 4), None),
        (([0, 0, 2, 2], 4), [2, 2]),
        (([-3, -2, -2, -1, 0, 1, 2, 3, 4], 4), [-2, -2]),
        (([-3, -2, -2, -1, 0, 1, 2, 3, 4], 0), [-3, 0]),
        (([-3, -2, -1, 0, 1, 2, 3, 4], 4), [1, 4]),
        (([0, 1, 2, 3], 0), [0, 1]),
        (([0, 0, 2, 3], 0), [0, 0]),
    ))
