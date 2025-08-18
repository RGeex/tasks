"""
Когда-то давно, а точнее во времена BASIC, существовало две функции с
названиями LEFT$ и RIGHT$ (я написал их заглавными буквами, потому
что так было принято в те далекие годы).

Эти функции позволяют считывать самые левые (/самые правые) символы строки.

    использовать: LEFT$ (str, i)-> возвращает iсамые левые символы str.

- eg:
A$="ABCDEFG":PRINT LEFT$(A$,3) - prints ABC

и RIGHT$ (str, i )конечно, возвращается iсамые правые символы str.
Итак, ваша миссия...

...написать 2 функции ( left$(str, i)& right$(str, i))
( left& rightв Ruby или Python ), которые будут работать так же, как и в
BASIC,... за исключением:

    iможет быть отрицательным целым числом. В этом случае функция возвращает
    всю строку , но iсамые правые(/левые) символы (соответственно в функции
    left$(/right$)).
    если i=== 0 : возвращает пустую строку;
    если нет iпредусмотрено, считайте, что это должно быть 1(не ноль).
    если iбольше чем strдлина : возвращает всю строку.

и

    если iэто string(да, может): возвращает часть strслева(/справа) от i.
        возвращается leftпервого ​ появления i
        возвращается rightпоследнего ​ появления i

Примеры:

text = 'Hello (not so) cruel World!'

left(text,5)   # -> 'Hello'
left(text,-22) # -> 'Hello'
left(text,1)   # -> 'H'
left(text)     # -> 'H' too
left(text,0)   # -> ''
left(text,99)  # -> 'Hello (not so) cruel World!'

right(text,6)  # -> 'World!'
right(text)    # -> '!'

#== with string as 2nd argument ==
left(text,'o') # -> 'Hell'
right(text,'o')# -> 'rld!'
left(text,' ') # -> 'Hello'  // -- string may be a space
"""
import typing
import unittest


def left(st: str, i: int | str = 1) -> str:
    """
    Возвращает левую часть строки до указанного символа.
    """
    return st[:st.index(i) if isinstance(i, str) else i]


def right(st: str, i: int | str = 1) -> str:
    """
    Возвращает правую часть строки до указанного символа.
    """
    return st[-(st[::-1].find(i[-1]) if isinstance(i, str) else i):] if i else ''


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(left, (
        (('Hello o o o  World', 5), 'Hello'),
        (('Hello o o o  World', 1), 'H'),
        (('Hello (not so) cruel World!', -22), 'Hello'),
        (('Hello', 'o'), 'Hell'),
    ))
    test(right, (
        (('Hello o o o  World',5), 'World'),
        (('Hello', 'e'), 'llo'),
    ))
