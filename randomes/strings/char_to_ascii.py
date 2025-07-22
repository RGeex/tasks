"""
Возьмите строку и верните хеш со всеми значениями ASCII символов в строке.
Возврат nil(Руби), None(Python) или null(JavaScript) если строка пустая.
Ключ — это символ, а значение — код ASCII этого символа.
Повторяющиеся символы, а также неалфавитные символы следует игнорировать. 
"""
import typing
import unittest


def char_to_ascii(st: str) -> dict[str, int] | None:
    """
    Создает словарь из ascii символов строки с их номером.
    """
    return {x: ord(x) for x in st if x.isalpha()} or None


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(char_to_ascii, (
        ("", None),
        ("a", {"a" : 97}),
        ("aaa", {"a" : 97}),
        ("hello world", {"h" : 104, "e" : 101, "l" : 108, "o" : 111, "w" : 119, "r" : 114, "d" : 100}),
        ("ABaa ^", {"A" : 65, "B" : 66, "a" : 97}),
    ))
