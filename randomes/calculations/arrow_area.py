"""
Площадь стрелки

Стрелка расположена внутри прямоугольника со сторонами a и b
соединяя нижние углы с серединой верхнего края и центром прямоугольника.

стрелка

a и b являются integers и > 0

Напишите функцию, которая возвращает площадь стрелки.


"""
import unittest
from typing import Any, Callable, Tuple


def arrow_area(a: int, b: int) -> int | float:
    """
    Определяет площадь треугольника.
    """
    return a * b / 4


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(arrow_area, (
        ((4, 2), 2),
        ((7, 6), 10.5),
        ((25, 25), 156.25),
    ))
