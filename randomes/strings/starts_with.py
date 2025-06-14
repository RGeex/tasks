"""
Испытание:
Даны две строки string и prefix, вернуть значение , string начинается ли оно с prefix,
как логическое значение.

Пример:
// string        prefix
"hello world!", "hello"    => true
"hello world!", "HELLO"    => false
"nowai",        "nowaisir" => false
Приложение:
В этой задаче для любого значения prefixвсегда должна возвращаться пустая строка .truestring

Если длина строки prefixбольше длины string, вернуть false.

Проверка должна быть чувствительна к регистру, т.е. "hello", "HE"должна возвращать false,
тогда как "hello", "he"должна возвращать true.

Ни один символ не должен игнорироваться и/или пропускаться во время теста, например,
пробельные символы не должны игнорироваться.
"""
import typing
import unittest


def starts_with(st: str, prefix: str) -> bool:
    """
    Проверяет, начинается ли строка с префикса.
    """
    return st.startswith(prefix)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(starts_with, (
        (("hello world!", "hello"), True),
        (("hello world!", "HELLO"), False),
        (("nowai", "nowaisir"), False),
        (("", ""), True),
        (("abc", ""), True),
        (("", "abc"), False),
        (("abc", "abcdef"), False),
        (("abc", "abc"), True),
        (("abcdef", "def"), False),
    ))
