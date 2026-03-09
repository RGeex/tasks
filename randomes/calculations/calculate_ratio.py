"""
Мы все ежедневно используем соотношения сторон 16:9, 16:10, 4:3 и т.д.
Главная задача — определить соотношение сторон изображения по его ширине и высоте.

Функция должна принимать ширину и высоту изображения и возвращать строку с
соотношением сторон (например, "16:9"). Если какой-либо из параметров ширины или
высоты равен 0, функция должна сгенерировать исключение (или вернуть значение). Nothing).

"""
import unittest
from typing import Any, Callable, Tuple


def calculate_ratio(w: int, h: int) -> str:
    """
    Определяет соотношщение сторон монитора по его разрешению.
    """
    return f'{w//x}:{h//x}' if w and h and (x := (gcd := lambda a, b: gcd(b, a % b) if b else a)(w, h)) else 'You threw an error'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calculate_ratio, (
        ((1024, 768), "4:3"),
        ((1920, 1080), "16:9"),
        ((600, 800), "3:4"),
        ((600, 600), "1:1"),
    ))
