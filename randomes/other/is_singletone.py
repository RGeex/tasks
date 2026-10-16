"""
В разработке программного обеспечения шаблон проектирования «синглтон» ограничивает создание
экземпляров класса одним объектом. Это полезно, когда для координации действий в системе необходим
ровно один объект.

Создайте класс таким образом, чтобы в сессии Singleton всегда существовал уникальный экземпляр этого
класса .Singleton

Пример:

a, b = Singleton(), Singleton()
isinstance(a, Singleton) # true
a is b # true
a.x = 5
b.x # 5
"""
import unittest
from typing import Any, Callable, Tuple


class Singleton:
    """
    Класс единого экземпляра.
    """
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    a, b, c = Singleton(), Singleton(), Singleton()
    test(lambda x: x, (
        (a is b, True),
        (b is c, True),
    ))
