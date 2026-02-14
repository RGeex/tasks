"""
Я дам вам целое число. Верните мне фигуру, длина и ширина которой равны этому числу. Это число будет целым числом от 1 до 50.
Пример

n = 3Таким образом, я ожидаю получить квадратную заднюю панель размером 3x3, как показано ниже, в виде строки:

+++
+++
+++

"""
import unittest
from typing import Any, Callable, Tuple


def generate_shape(n: int) -> str:
    """
    Рисует фигуру по заданному параметру.
    """
    return '\n'.join(['+' * n] * n)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(generate_shape, (
        (3, '+++\n+++\n+++'),
        (8, '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'),
    ))
