"""
Задача

Имея массив чисел и индекс, верните либо индекс наименьшего числа, большего,
чем элемент с заданным индексом, либо -1если такого индекса нет
(или, если применимо, Nothingили аналогичное пустое значение).
Примечания

Возможны несколько правильных ответов. В этом случае верните любой из них.
Указанный индекс будет находиться внутри указанного массива.
Таким образом, данный массив никогда не будет пустым.
Пример

least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1

"""
import unittest
from typing import Any, Callable, List, Tuple


def least_larger(a: List[int], i: int) -> int:
    """
    Поиск минимального числа слудующего за указанным индексом.
    """
    return a.index(min(x)) if (x := [x for x in a if x > a[i]]) else -1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(least_larger, (
        (([4, 1, 3, 5, 6], 0), 3 ),
        (([4, 1, 3, 5, 6], 4), -1 ),
        (([1, 3, 5, 2, 4], 0), 3 ),
    ))
