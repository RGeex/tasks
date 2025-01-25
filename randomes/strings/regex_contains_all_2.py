"""
Задача:

Ваша функция должна возвращать допустимое регулярное выражение. Это шаблон, который обычно
используется для сопоставления частей строки. В этом случае будет использоваться для проверки
того, все ли символы, указанные во входных данных, присутствуют в строке.
Вход

Непустая строка уникальных символов алфавита в верхнем и нижнем регистре.
Выход

Строка шаблона регулярного выражения.
Примеры

Ваша функция должна возвращать строку.

# Function example
def regex_contains_all(st): 
  return r"abc"

Этот шаблон регулярного выражения будет проверен следующим образом.

# Test
abc = 'abc'
pattern = regex_contains_all(abc)
st = 'zzzaaacccbbbzzz'
bool(re.match(pattern, st), f"Testing if {st} contains all characters in {abc} with your pattern
{pattern}") -> True
"""
import re
import typing
import unittest


def regex_contains_all(st: str) -> str:
    """
    Создает регулярное выражение для поиска всех заданных символов в строке.
    """
    return ''.join([f'(?=.*{x})' for x in st])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(bool(re.match(func(key[0]), key[1])), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(regex_contains_all, (
        (('abc', 'bca'), True),
        (('abc', 'baczzz'), True),
        (('abc', 'ac'), False),
        (('abc', 'bc'), False),
        (('abc', 'cb'), False),
    ))
