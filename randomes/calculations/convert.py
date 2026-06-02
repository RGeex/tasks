"""
Преобразование десятичных градусов в градусы, минуты и секунды.

Запомните: 1 градус = 60 минут; 1 минута = 60 секунд.

Входные данные: Положительное число.

Вывод: Массив [градусы, минуты, секунды]. Например: [30, 25, 25]

В выходных данных следует опускать нули в конце. Например:

convert (50) 
//correct output -> [50] 
//wrong output -> [50, 0, 0]

convert(80.5)
//correct output -> [ 80, 30 ]
//wrong output -> [80, 30, 0]

convert(0.0001388888888888889)
//correct output -> [ 0, 0, 1 ]
//wrong output -> [1]

Округлите секунды до ближайшего целого числа.



"""
import unittest
from typing import Any, Callable, List, Tuple


def convert(degrees: int | float) -> List[int]:
    """
    Преобразование десятичных градусов в градусы, минуты и секунды.
    """
    t = int(degrees * 3600)
    d, m, s = t // 3600, t % 3600 // 60, t % 60
    return [d, m, s] if s else [d, m] if m else [d]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(convert, (
        (0, [0]),
        (40.567, [40, 34, 1]),
        (80.5, [80, 30]),
        (20.999, [20, 59, 56]),
        (50, [50]),
        (0.0001388888888888888, [0]),
        (91.33333333333333, [91, 20]),
    ))
