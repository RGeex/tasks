"""
Напишите функцию, которая возвращает последовательность (индекс начинается с 1)
всех четных символов строки. Если строка короче двух символов или длиннее 100
символов, функция должна вернуть "недопустимая строка".

Например:

"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"
"""
import typing
import unittest


def even_chars(st: str) -> list[str] | str:
    """
    Возвращает список нечетных символов строки, если длина строки больше 1 и меньше 100 символов.
    """
    return [x for i, x in enumerate(st) if i % 2] if 1 < len(st) < 100 else "invalid string"
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(even_chars, (
        ("a", "invalid string"),
        ("abcdefghijklm", ["b", "d", "f", "h", "j", "l"]),
        ("aBc_e9g*i-k$m", ["B", "_", "9", "*", "-", "$"]),
    ))
