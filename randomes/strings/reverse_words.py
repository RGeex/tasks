"""
Заполните функцию, которая принимает параметр строки, и меняет каждое слово в строке.
Все места в строке должны быть сохранены.
Примеры

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"


"""
import re
import typing
import unittest


def reverse_words(text: str) -> str:
    """
    Инвертирует каждое слово в строке.
    """
    return re.sub(r'\w*[^ ]', lambda x: x.group(0)[::-1], text)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_words, (
        ('The quick brown fox jumps over the lazy dog.', 'ehT kciuq nworb xof spmuj revo eht yzal .god'),
        ('apple', 'elppa'),
        ('a b c d', 'a b c d'),
        ('  double  spaced  words  ', '  elbuod  decaps  sdrow  '),
    ))
