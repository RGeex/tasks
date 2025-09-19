"""
Для каждой строки, после каждого появления 'and'и/или 'but', вставьте
подстроку 'apparently'непосредственно после происшествия(й).

Если входные данные не содержат «and» или «but», вернуть ту же строку.
Если строка пустая, вернуть ''.

Если подстрока 'apparently'уже сразу после 'and'и/или 'but', не добавляйте
еще один. (Не добавляйте дубликаты).
Примеры:

Вход 1

'It was great and I've never been on live television before but sometimes
I don't watch this.'

Выход 1

'It was great and apparently I've never been on live television before but
apparently sometimes I don't watch this.'

Вход 2

'but apparently'

Выход 2

'but apparently' 

(без изменений, потому что 'apparently'уже сразу после 'but'и не должно быть
дубликатов.)

Возникновение 'and'и/или 'but'Учитывается только если оно разделено хотя бы
одним пробелом. Например: 'andd' и 'bbut'не считаются событиями, тогда как 'b but'
и 'and d'имеет значение.
"""
import typing
import unittest
import re


def apparently(st: str) -> str:
    """
    Дополняет предложение словами, если соблюдается условие.
    """
    return re.sub(r'(?i)\b(and|but)\b(?!\s+apparently\b)', r'\1 apparently', st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(apparently, (
        ('It was great and I have never been on live television before but sometimes I dont watch this.', 'It was great and apparently I have never been on live television before but apparently sometimes I dont watch this.'),
        ('and apparently', 'and apparently'),
        ('and', 'and apparently'),
        ('apparently', 'apparently'),
    ))
