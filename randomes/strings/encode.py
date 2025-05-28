"""
Напишите функцию, которая принимает строку и заменяет все буквы на их соответствующие позиции в
английском алфавите, например: 'a' является 1, 'z' является 26. Функция не должна учитывать
регистр.

'abc'      --> '123'
'ABC'      --> '123'
'codewars' --> '315452311819'
'abc-#@5'  --> '123-#@5'

"""
import typing
import unittest
from string import ascii_lowercase as abc


def encode(st: str) -> str:
    """
    Заменяет в стоке буквы алфавита на их порядковый номер, не зависимо от регистра.
    Прочие символы не изменяются.
    """
    return ''.join(str(abc.index(x) + 1) if x in abc else x for x in st.lower())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(encode, (
        ('abc','123'),
        ('ABCD','1234'),
        ('ZzzzZ','2626262626'),
        ('abc-#@5','123-#@5'),
        ('this is a long string!! Please [encode] @C0RrEctly','208919 919 1 1215147 1920189147!! 161251195 [51431545] @30181853201225'),
    ))
