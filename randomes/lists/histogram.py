"""
Вам будет предоставлен массив неотрицательных целых чисел с положительной шириной ячейки.

Ваша задача — создать метод Histogram, который будет возвращать данные гистограммы,
соответствующие входному массиву. Данные гистограммы представляют собой массив,
в котором под индексом i хранится количество чисел, принадлежащих ячейке i.
Первая ячейка всегда начинается с нуля.

При пустом вводе следует вернуть пустой вывод.

Примеры:

    Для входных данных [1, 1, 0, 1, 3, 2, 6] и binWidth=1 результат будет [1, 3, 1, 1, 0, 0, 1],
    поскольку данные содержат один элемент "0", три элемента "1" и т. д.
    При тех же данных и binWidth=2 результат будет [4, 2, 0, 1]
    Для входных данных [7] и binWidth=1 результат будет [0, 0, 0, 0, 0, 0, 0, 1]

"""
import unittest
from typing import Any, Callable, List, Tuple


def histogram(values: List[int], bin_width: int) -> List[int]:
    """
    Cоздаtn метод Histogram, который возвращаtn данные гистограммы, соответствующие входному массиву.
    """
    return [sum(n in range(x, bin_width + x) for n in values) for x in range(0, max(values, default=-1) + 1, bin_width)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(histogram, (
        (([1, 1, 0, 1, 3, 2, 6], 1), [1, 3, 1, 1, 0, 0, 1]),
        (([1, 1, 0, 1, 3, 2, 6], 2), [4, 2, 0, 1]),
        (([], 1), []),
        (([8], 1), [0, 0, 0, 0, 0, 0, 0, 0, 1]),
    ))
