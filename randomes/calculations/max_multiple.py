"""
Задача
Дан делитель и его граница . Найдите наибольшее целое число N такое, что .

Условия :
N делится на делитель

N меньше или равно границе

N больше 0 .

Примечания
Параметры (делитель, граница), передаваемые функции, являются только положительными значениями .
Гарантируется, что делитель найден .
Примеры ввода и вывода
divisor = 2, bound = 7 ==> return (6)
Объяснение:
(6) делится на (2) , (6) меньше или равно границе (7) , и (6) > 0.

divisor = 10, bound = 50 ==> return (50)
Объяснение:
(50) делится на (10) , (50) меньше или равно границе (50) , и (50) > 0.*

divisor = 37, bound = 200 ==> return (185)
Объяснение:
(185) делится на (37) , (185) меньше или равно границе (200) , и (185) > 0.
"""
import unittest
from typing import Any, Callable, Tuple


def max_multiple(divisor: int, bound: int) -> int:
    """
    Поиск наибольшего N удовлетворяющих условию.
    """
    return bound // divisor * divisor


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_multiple, (
        ((2, 7), 6),
        ((3, 10), 9),
        ((7, 17), 14),
        ((10, 50), 50),
        ((37, 200), 185),
        ((7, 100), 98),
    ))
