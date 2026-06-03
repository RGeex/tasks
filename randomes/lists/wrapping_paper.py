"""
Вы разрабатываете утилиту, которая рассчитывает общее количество упаковочной бумаги,
необходимой для набора прямоугольных коробок.

Каждый прямоугольник определяется тремя целочисленными размерами:
длиной (l), шириной (w) и высотой (h).

Для каждой коробки требуется следующее количество оберточной бумаги:

    Площадь поверхности коробки
    Плюс запас, равный площади самой короткой стороны.

Вход: Список ячеек, где каждая ячейка представлена ​​в виде кортежа или объекта,
содержащего три целых числа (l, w, h).

Выход: Целое число, обозначающее общее количество оберточной бумаги,
необходимое для всех коробок в списке.

"""
import unittest
from typing import Any, Callable, List, Tuple
from itertools import combinations as cb
from operator import mul


def wrapping_paper(boxes: List[Tuple[int]]) -> int:
    """
    Определяет общее количество оберточной бумаги, необходимое для всех коробок в списке.
    """
    return sum(sum(mul(*x) * [2, 3][not i] for i, x in enumerate(cb(sorted(x), 2))) for x in boxes)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(wrapping_paper, (
        ([(2, 3, 4)], 58),
        ([(10, 1, 1)], 43),
        ([(2, 3, 4), (1, 1, 1)], 58 + 7),
    ))
