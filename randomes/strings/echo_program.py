"""
Напишите echoProgram функция (или echo_program(зависит от языка), который возвращает исходный код вашего решения в виде строки.
"""
import typing
import unittest


def echo_program() -> str:
    """
    Возвращает исходный код функции в виде строки.
    """
    return open(__file__).read()


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(lambda x: x, (
        (hasattr(echo_program, '__call__'), True),
        (isinstance(echo_program(), str), True),
    ))
