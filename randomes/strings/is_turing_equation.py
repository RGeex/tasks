"""
Задача

Вам дана строка s. Это уравнение типа "a+b=c", где a, b, c — числа, состоящие
из цифр от 0 до 9. Это включает возможные начальные и конечные нули.
Уравнения не будут содержать пробелов.

Ваша задача — определить, s является допустимым уравнением Тьюринга.
Возврат true или false, соответственно, в интерпретации Тьюринга, т.е.
числа читаются в обратном порядке.

Всё ещё не понимаете задание? Посмотрите на следующие примеры ;-)
Примеры

Для s = "73+42=16", выход должен быть true.

73 -> 37
42 -> 24
16 -> 61
37+24==61

Для s = "5+8=13", выход должен быть false.

5 -> 5
8 -> 8
13 -> 31
5+8!=31

Для s = "10+20=30", выход должен быть true.

10 -> 01 -> 1
20 -> 02 -> 2
30 -> 03 -> 3
1+2==3

Примечание

    Все числа a, b, c не более 10 цифр, не считая начальных нулей (читаются в обратном порядке)

    sсодержит только цифры, «+» и «=», "-","*" or "/"не будет отображаться в строке.

    Счастливого кодирования ^_^
"""
import typing
import unittest
import re


def is_turing_equation(s: str) -> bool:
    """
    Проверяет, является ли строка допустимым уравнением Тьюринга.
    """
    a, *b = map(int, re.sub(r'[\+\=]', ' ', s[::-1]).split())
    return sum(b) == a


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_turing_equation, (
        ('73+42=16',True),
        ('5+8=13',False),
        ('10+20=30',True),
        ('0001000+000200=00030',True),
        ('1234+5=1239',False),
        ('1+0=0',False),
        ('7000+8000=51',True),
        ('0+0=0',True),
    ))
