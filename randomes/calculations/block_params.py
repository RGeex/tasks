"""
Напишите класс Blockэто создает блокировку (ну, это же очевидно...).
Требования

Конструктор должен принимать в качестве аргумента массив. Это будет содержать 3 целых числа
вида [width, length, height]из которого Blockего следует создать.

Определите следующие методы:

`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`

Примеры

    b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
    
    b.get_width() -> return 2
    
    b.get_length() -> return 4
    
    b.get_height() -> return 6
    
    b.get_volume() -> return 48
    
    b.get_surface_area() -> return 88

"""
import unittest
from typing import Any, Callable, List, Tuple


class Block:
    """
    Расчет параметров блока.
    """
    def __init__(self, arr: List[int]) -> None:
        self.width, self.length, self.height,  = arr

    def get_width(self) -> int:
        """
        Ширина блока.
        """
        return self.width

    def get_length(self) -> int:
        """
        Длина блока.
        """
        return self.length

    def get_height(self) -> int:
        """
        Высота блока.
        """
        return self.height

    def get_volume(self) -> int:
        """
        Объем блока.
        """
        return self.width * self.length * self.height

    def get_surface_area(self) -> int:
        """
        Площадь поверхностей блока.
        """
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    block = Block([2, 2, 2])
    test(lambda x: x, (
        (block.get_width(), 2),
        (block.get_length(), 2),
        (block.get_height(), 2),
        (block.get_volume(), 8),
        (block.get_surface_area(), 24),
    ))
