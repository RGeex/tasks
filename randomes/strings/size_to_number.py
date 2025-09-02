"""
Описание

У вас есть одежда международного размера в виде текста ( xs, s, xxl).
Ваша цель — вернуть европейский размер числа в виде числа, соответствующего этому размеру.

Обратите внимание, что существует произвольное количество модификаторов ( x),
за исключением mразмер и входные данные могут быть любой строкой.
Линейность

Базовый размер для среднего ( m) является 38.
(тогда, маленький ( s) является 36, и большой ( l) является 40)

Шкала линейная; модификатор xпродолжает, добавляя или вычитая 2от полученного размера.

(Для размеров, где xмодификатор делает общий размер отрицательным,
воспринимайте это как нормально и возвращайте отрицательный размер)
Недопустимые случаи

Функция должна обрабатывать неправильные/недопустимые размеры.

Допустимый входной сигнал имеет любой базовый размер ( s/ m/ l) и любое
количество модификаторов ( x) перед базовым размером (например xxl).
Обратите внимание, что вы не можете применить модификатор для mразмер,
считать этот случай недействительным!
Все остальное запрещено и должно считаться недействительным
( Noneдля Python, 0, falseдля Го, nullдля JavaScript).

Неверные примеры: xxx, sss, xm, other string
Допустимые примеры

xs: 34
s: 36
m: 38
l: 40
xl: 42
"""
import typing
import unittest
import re


def size_to_number(size: str) -> int | None:
    """
    Определяет размер вещи по европейскому стандарту.
    """
    return re.match(r'^(x*[sl]|m)$', size) and 'sml'.index(size[-1]) * 2 + 36 + size.count('x') * [-2, 2][size[-1] == 'l']


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(size_to_number, (
        ("s", 36),
        ("m", 38),
        ("l", 40),
        ("xl", 42),
        ("xs", 34),
        ("xxxs", 30),
        ("xxxl", 46),
        ("", None),
        ("xm", None),
        ("xxxm", None),
        ("xxxx", None),
        ("ssss", None),
        ("hello world", None),
        ("sm", None),
        ("ml", None),
        ("lm", None),
    ))
