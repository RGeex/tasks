"""
Задача
Вы только что переехали на совершенно прямую улицу с абсолютно nодинаковыми домами по обеим
сторонам дороги. Естественно, вам хотелось бы узнать номер дома людей, живущих на другой
стороне улицы. Улица выглядит примерно так:

Улица
1|   |6
3|   |4
5|   |2
  you
Четные числа увеличиваются справа; нечетные — слева. Номера домов начинаются с 1и увеличиваются без
пробелов. Когда n = 3, 1противоположно 6, 3противоположно 4и 5противоположно 2.

Пример (адрес, n --> выход)
Зная номер вашего дома addressи длину улицы n, укажите номер дома на противоположной стороне улицы.

1, 3 --> 6
3, 3 --> 4
2, 3 --> 5
3, 5 --> 8
"""
import unittest
from typing import Any, Callable, Tuple


def over_the_road(address: int, n: int) -> int:
    """
    определяет номер дома на противоположной стороне.
    """
    return n * 2 - (address - address % 2) + (not address % 2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(over_the_road, (
        ((1, 3), 6),
        ((3, 3), 4),
        ((2, 3), 5),
        ((3, 5), 8),
        ((7, 11), 16),
        ((23633656673, 310027696726), 596421736780),
    ))
