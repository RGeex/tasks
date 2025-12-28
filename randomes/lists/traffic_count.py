"""
Вы работаете в компании, которая анализирует количество транспортных средств на определенном
перекрестке в часы пик с 16:00 до 20:00. Каждый день вам предоставляется список, содержащий
количество автомобилей, проезжающих через перекресток каждые 10 минут с 16:00 до 20:00.

Вам необходимо вернуть список кортежей, каждый из которых содержит время и максимальный объем
трафика за каждый час.

Например:

a1 = [23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]

traffic_count(a1) ==> [('4:00pm', 45), ('5:00pm', 65), ('6:00pm', 89), ('7:00pm', 93)]

Все значения в данном списке являются целыми числами.
"""
import unittest
from typing import Any, Callable, Dict, List, Tuple


def traffic_count(array: List[int]) -> List[Tuple[str, int]]:
    """
    Учитывает трафик за каждый час с 16:00 до 20:00.
    """
    return [(f'{4 + i}:00pm', max(array[i * 6:i * 6 + 6])) for i in range(len(array) // 6)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(traffic_count, (
        (
            [23, 24, 34, 45, 43, 23, 57, 34, 65, 12, 19, 45, 54, 65, 54, 43, 89, 48, 42, 55, 22, 69, 23, 93],
            [('4:00pm', 45), ('5:00pm', 65), ('6:00pm', 89), ('7:00pm', 93)],
        ),
        (
            [22, 31, 70, 22, 49, 62, 38, 26, 44, 43, 67, 30, 76, 77, 18, 47, 42, 57, 30, 38, 87, 94, 7, 18],
            [('4:00pm', 70), ('5:00pm', 67), ('6:00pm', 77), ('7:00pm', 94)],
        ),
    ))
