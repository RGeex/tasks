"""
Вам дан набор шестигранных игральных костей. Каждая кость представлена ​​лицевой стороной вверх.

Рассчитайте минимальное количество поворотов, необходимых для того,
чтобы все грани стали одинаковыми.

12Для того чтобы лицевая сторона оказалась сверху , потребуется один поворот 3,
4а 5для того, чтобы она стала лицевой стороной , потребуется два поворота 6,
так как 6это противоположная сторона 1.

Противоположная сторона — 2это 5и 3есть 4.

Примеры
dice = {1, 1, 1, 1, 1, 6} --> 2:
rotate 6 twice to get 1

dice = {1, 2, 3} --> 2:
2 rotations are needed to make all faces either 1, 2, or 3

dice = {3, 3, 3} --> 0:
all faces are already identical

dice = {1, 6, 2, 3} --> 3:
"""
import unittest
from typing import Any, Callable, List, Tuple


def count_min_rotations(dices: List[int]) -> int:
    """
    Рассчитает минимальное количество поворотов, необходимых для того, чтобы все грани стали одинаковыми.
    """
    return min([sum((x+dice == 7)+(x != dice) for x in dices) for dice in set(dices)])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_min_rotations, (
        ([1, 1, 6],     2),
        ([1, 2, 3],     2),
        ([3, 3, 3],     0),
        ([1, 6, 2, 3],  3),
    ))
