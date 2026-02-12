"""
Сможет ли Санта спасти Рождество?

О нет! Маленькие эльфы Санты в этом году заболели. Ему придётся раздавать подарки самому.

Но у него осталось всего 24 часа. Сможет ли он это сделать?
Ваша задача:

В качестве входных данных вы получите массив, содержащий продолжительность времени в виде строк в
следующем формате: HH:MM:SSКаждый параметр обозначает время, необходимое Санте для доставки подарка.
Определите, сможет ли он сделать это за 24 часа или нет. Если на доставку всех подарков потребуется
ровно 24 часа, Санта сможет завершить доставку ;-).
"""
import unittest
from typing import Any, Callable, List, Tuple
from datetime import datetime as dt, timedelta as td


def determine_time(arr: List[str]) -> bool:
    """
    Определяет, успеет ли санта доставить все подарки вовремя.
    """
    return sum([dt.strptime(x, '%H:%M:%S') - dt(1900, 1, 1) for x in arr], td()) <= td(days=1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(determine_time, (
        (["01:00:00", "02:30:00"], True),
		(["01:00:00", "02:30:00", "22:00:00"], False),
		(["12:00:00", "12:00:00"] , True),
		([], True),
    ))
