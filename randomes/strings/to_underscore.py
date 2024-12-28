"""
Завершите функцию/метод так, чтобы она заняла PascalCase строку и возвращает
строку в snake_case обозначения. Символы нижнего регистра могут быть числами.
Если метод получает на вход число, он должен вернуть строку.
Примеры

"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
"""
import re
import typing


def to_underscore(st: str | int) -> str:
    """CamelCase to snake_case."""
    return re.sub(r'([A-Z])', lambda m: f'_{m.group(1).lower()}', str(st)).strip('_')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(to_underscore, (
        (1, "1"),
        ("App7Test", "app7_test"),
        ("TestController", "test_controller"),
        ("MoviesAndBooks", "movies_and_books"),
    ))
