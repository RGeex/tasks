"""
Напишите метод, который, получив два аргумента, width и heightВозвращает строку,
представляющую прямоугольник с указанными размерами.

Прямоугольник должен быть заполнен пробелами, а его границы должны состоять из звездочек ( *).

Например, при условии width = 3 и height = 3:

***
* *
***

Завершайте каждую строку строки (включая последнюю) комбинацией возврата каретки и перевода строки.

Примечание: можно предположить, что ширина и высота всегда будут больше нуля.


"""
import unittest
from typing import Any, Callable, Tuple


def get_rectangle_string(width: int, height: int) -> str:
    """
    Рисует прямоугольник с заданными сторонами.
    """
    return (f'*{" " * (width - 2)}*\r\n' * (height - 2)).join([f'{"*" * width}\r\n'] * 2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_rectangle_string, (
        ((3, 3), "***\r\n* *\r\n***\r\n"),
        ((4, 5), "****\r\n*  *\r\n*  *\r\n*  *\r\n****\r\n"),
        ((1, 2), "*\r\n*\r\n"),
    ))
