"""
В этом простом примере ваша функция должна принимать строку на вход и
возвращать строку, из которой удалено всё ( включая пробелы ), кроме цифр.
Как вы, возможно, догадались, пустые строки возвращаются без изменений,
а если входная строка не содержит цифр, то на выходе будет пустая строка
следует следить за нестроковыми . Кстати, вам также входными данными.
Для них возвращайте «Недопустимый ввод!» .

digit_all("are_you_kidding_me_???") --------------> ''   
digit_all("wai8, where are you goin'?") ----------> '8'   
digit_all("") ------------------------------------> ''   
digit_all(['yes','i','am','kidding','you','!']) --> 'Invalid input !'   
digit_all("1 2 3       4") -----------------------> '1234'
"""
import typing
import unittest
import re
from typing import Any


def digit_all(x: Any) -> str:
    """
    Убирает из строки все символы кроме цифр, если передана строка или сообщение об ошибке.
    """
    return re.sub(r'[^\d]', '', x) if isinstance(x, str) else 'Invalid input !'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(digit_all, (
        ("are_you_kidding_me_???",''),
        ("wai8, where are you goin'?",'8'),
        ("",''),
        (['yes','i','am','kidding','you','!'],'Invalid input !'),
        (False,'Invalid input !'),
        (None,'Invalid input !'),
        (True,'Invalid input !'),
        (1234,'Invalid input !'),
        (['abcde'],'Invalid input !'),
        ('a1b2c3d4e','1234'),
        ('are_you_kidding_me_???',''),
        ('                     4','4'),
        ('                     ',''),
    ))
