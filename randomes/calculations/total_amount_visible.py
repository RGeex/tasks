"""
Ваша задача — вернуть количество видимых точек на игральной кости после броска
(то есть общее количество точек, которые не касались бы игральной кости при броске).

В качестве входных данных для параметра "numOfSides"
можно использовать 6, 8, 10, 12, 20-гранные игральные кости.

Параметр topNum равен числу, которое находится сверху, или числу, которое выпало на кубике.

В этом упражнении сумма чисел на противоположных сторонах равна 1, что на 1 больше,
чем общее количество сторон. Например: на шестигранной игральной кости напротив единицы
окажется 6, напротив тройки — 4 и так далее. В этом упражнении десятигранная игральная
кость начинает выпадать с 1 и заканчивается на 10.

Примечание: значение topNum никогда не будет больше, чем numOfSides.
"""
import unittest
from typing import Any, Callable, Tuple


def total_amount_visible(top_num: int, num_of_sides: int) -> int:
    """
    Определяет сумму чисел видимых точек на кубике.
    """
    return sum(range(num_of_sides + 1)) - (num_of_sides - top_num + 1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(total_amount_visible, (
        ((3, 6), 17),
        ((3, 8), 30),
        ((1, 12), 66),
    ))
