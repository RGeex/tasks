"""
Путешествуя по интернету, я наткнулся на интересную математическую задачу под
названием «Всегда идеально». Это означает, что если к произведению четырёх
последовательных чисел прибавить 1, ответ ВСЕГДА будет точным квадратом.
Например, у нас есть: 1, 2, 3, 4, и произведение будет 1 × 2 × 3 × 4 = 24.
Если к произведению прибавить 1, то получится 25, поскольку полученное число —
полный квадрат, квадратный корень из 25 будет равен 5.

Теперь давайте напишем функцию, которая принимает числа, разделенные запятыми,
в строковом формате и возвращает число, являющееся полным квадратом, и квадратный
корень этого числа.

Если строка содержит символы, отличные от числа, или содержит больше или
меньше 4 цифр, разделенных запятой, функция возвращает «неверный ввод».

Если строка содержит 4 цифры, но не последовательные, возвращается
«не последовательные».
"""
import typing
import unittest
import re
from operator import mul
from functools import reduce


def check_root(st: str) -> str:
    """
    Если строка соответствует заданному шаблону выводит произведение чисел + 1
    и корень из этого числа или сообщение об ошибке.
    """
    if re.match(r'^-?\d+,-?\d+,-?\d+,-?\d+$', st):
        lst = list(map(int, st.split(",")))
        if next((0 for i, n in enumerate(lst, lst[0]) if n != i), 1):
            return f'{(x := reduce(mul, lst) + 1)}, {int(x ** .5)}'
        return 'not consecutive'
    return 'incorrect input'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(check_root, (
        ('4,5,6,7', '841, 29'),
        ('3,s,5,6', 'incorrect input'),
        ('11,13,14,15', 'not consecutive'),
        ('10,11,12,13,15', 'incorrect input'),
        ('10,11,12,13', '17161, 131'),
        ('ad,d,q,tt,v', 'incorrect input'),
        ('//,;;,/,..,', 'incorrect input'),
        ('1,2,3,4', '25, 5'),
        ('1015,1016,1017,1018', '1067648959441, 1033271'),
        ('555,777,444,111', 'not consecutive'),
        ('20,21,22,24', 'not consecutive'),
        ('9,10,10,11', 'not consecutive'),
        ('11254,11255,11256,11258', 'not consecutive'),
        ('25000,25001,25002,25003', '390718756875150001, 625075001'),
        ('2000000,2000001,2000002,2000003', '16000048000044000012000001, 4000006000001'),
        ('4,5,6,q', 'incorrect input'),
        ('5,6,7', 'incorrect input'),
        ('3,5,6,7', 'not consecutive'),
        ('-4,-3,-2,-1', '25, 5'),
        ('-1,0,1,2', '1, 1'),
    ))
