"""
Вам дана строка, содержащая 0, 1 и один или несколько символов «?», где ? это подстановочный знак,
который может быть 0 или 1.

Верните массив, содержащий все возможности, которых вы можете достичь, заменив ? за ценность.
Примеры

'101?' -> ['1010', '1011']

'1?1?' -> ['1010', '1110', '1011', '1111']

Примечания:

    Не беспокойтесь о сортировке вывода.
    Ваша строка никогда не будет пустой.
"""
import typing
from itertools import product


def possibilities(st: str) -> list[str]:
    """
    Создает все возможные комбинации заданного двоичного числа, заменяя "?" - "цифрами."
    """
    return [st.replace('?', '{}').format(*x) for x in product('01', repeat=st.count('?'))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(possibilities, (
        ('101?', ['1010', '1011']),
        ('10??', ['1000', '1001', '1010', '1011']),
        ('1?1?', ['1010', '1011', '1110', '1111']),
    ))
