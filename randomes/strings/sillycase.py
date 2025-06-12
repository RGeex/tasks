"""
Создайте функцию, которая принимает строку и возвращает ее. строка,
в которой первая половина написана строчными буквами, а вторая — заглавными.

например: foobar == fooBAR

Если это нечетное число, то «округлите» его, чтобы узнать, какие буквы следует
сделать заглавными. Смотрите пример ниже.

sillycase("brian")  
//         --^-- midpoint  
//         bri    first half (lower-cased)  
//            AN second half (upper-cased)  
"""
import typing
import unittest


def sillycase(silly: str) -> str:
    """
    Первую половину символов переданной строки переводит в нижний регистр,
    Вторую половину в верхний регистр.
    """
    x = sum(divmod(len(silly), 2))
    return silly[:x].lower() + silly[x:].upper()


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sillycase, (
        ('foobar', "fooBAR"),
        ('codewars', "codeWARS"),
        ('jAvASCript', "javasCRIPT"),
        ('brian', 'briAN'),
        ('jabberwock', 'jabbeRWOCK'),
        ('SCOTland', 'scotLAND'),
        ('WeLlDoNe', 'wellDONE'),
    ))
