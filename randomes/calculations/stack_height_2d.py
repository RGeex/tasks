"""
Фон
Я сложил несколько бильярдных шаров в треугольник.

Так,

бильярдные шары
Задание Ката
Учитывая количество элементов layersв моей стопке, какова её общая высота?

Верните высоту, равную числу, кратному диаметру шара.

Пример
На изображении выше показана стопка из 5 слоев.

Примечания
layers>= 0
Приблизительные ответы (с точностью до 0,001) считаются достаточно точными.
"""
import unittest
from typing import Any, Callable, Tuple


def stack_height_2d(layers: int) -> int:
    """
    Определяет высоту стопки.
    """
    return round((1 + 3**0.5 * (layers - 1) / 2), 3) if layers > 0 else 0


def stack_height_2d_2(layers: int) -> int:
    """
    Определяет высоту стопки.
    """
    return layers and 1 + (layers - 1) * ((3**.5) / 2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(stack_height_2d, (
        (1, 1),
    ))
    test(stack_height_2d_2, (
        (1, 1),
    ))
