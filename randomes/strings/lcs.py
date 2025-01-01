"""
Напишите функцию под названием LCS который принимает две последовательности и возвращает самую
длинную подпоследовательность, общую для переданных последовательностей.
Подпоследовательность

Подпоследовательность отличается от подстроки. Члены подпоследовательности не обязательно должны
быть последовательными членами исходной последовательности.
Пример подпоследовательности

Подпоследовательности "abc" = "a", "b", "c", "ab", "ac", "bc" и "abc".
Примеры LCS

lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"

Примечания

    Оба аргумента будут строками
    Возвращаемое значение должно быть строкой
    Возвращает пустую строку, если не существует общей подпоследовательности.
    Оба аргумента будут иметь один или несколько символов (в JavaScript).
    Все тесты будут иметь только одну самую длинную общую подпоследовательность. Не беспокойтесь о
    таких случаях, как LCS( "1234", "3412" ), который будет иметь две возможные самые длинные общие
    подпоследовательности: "12" и "34".

Обратите внимание, что вариант Haskell будет использовать рандомизированное тестирование, но
допустимой будет любая самая длинная общая подпоследовательность.

Обратите внимание, что вариант OCaml использует общие списки вместо строк, а также будет иметь
рандомизированные тесты (любая самая длинная общая подпоследовательность будет допустимой).
"""
import typing


def lcs(a: str, b: str) -> str:
    """
    Поиск максимальнодй длины подпоследовательности общей у 2-х строк.
    """
    r = sorted(set().union(*map(set, e := [[i for i, v in enumerate(b) if v == x] for x in a if x in b])))
    return ''.join([b[x[0]] for i, v in enumerate(r) if (x := next((x for x in e[i:] if v in x), 0))])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(lcs, (
        (("a", "b"), ""),
        (("a", "a"), "a"),
        (("abc", "ac"), "ac"),
        (("abcdef", "abc"), "abc"),
        (("abcdef", "acf"), "acf")        ,
        (("anothertest", "notatest"), "nottest"),
        (("132535365", "123456789"), "12356"),
        (("finaltest", "zzzfinallyzzz"), "final"),
    ))
