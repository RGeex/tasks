"""
Предположим, нам нужны "чистые" строки. Чистые означает, что строка должна содержать
только буквы a-z, A-Zи пробелы. Мы предполагаем, что нет двойных пробелов или переносов строк.

Напишите функцию, которая принимает строку и возвращает строку без ненужных символов.
Примеры

'.tree1'                     ==> 'tree'
"that's a pie$ce o_f p#ie!"  ==> 'thats a piece of pie'
'john.dope@dopington.com'    ==> 'johndopedopingtoncom'
'my_list = ["a","b","c"]'    ==> 'mylist  abc'
'1 + 1 = 2'                  ==> '    '
"0123456789.+,|[]{}=@/~;^$'<>?-!*&:#%_"  ==> ''
"""
import typing
import unittest


def remove_chars(st: str) -> str:
    """
    Удаляет из строки все символы кроме букв и пробелов.
    """
    return ''.join(x for x in st if x.isalpha() or x == ' ')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_chars, (
        ('co_ol f0un%(c)t-io"n', "cool function"),
        ("test for error!", "test for error"),
        (".tree1", 'tree'),
        ("that's a pie&ce o_f p#ie!", 'thats a piece of pie'),
    ))
