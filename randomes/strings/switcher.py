"""
Вам необходимо вернуть строку, имея массив чисел (в строковом формате).
Числа соответствуют буквам алфавита в обратном порядке: a=26, z=1 и т.д.
Также следует учитывать '!', '?' и ' 'которые представлены числами «27», «28» и «29» соответственно.

Все введенные данные будут действительными.

"""
import typing
import unittest
from string import ascii_lowercase as abc


def switcher(arr: list[str], more: str = '!? ') -> str:
    """
    Создает строку из набора чисел.
    """
    return ''.join(map(dict(enumerate(abc[::-1] + more, 1)).get, map(int, arr)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(switcher, (
        (['24', '12', '23', '22', '4', '26', '9', '8'], 'codewars'),
        (['25','7','8','4','14','23','8','25','23','29','16','16','4'], 'btswmdsbd kkw'),
        (['4', '24'], 'wc'),
        (['12'], 'o'),
        (['12','28','25','21','25','7','11','22','15'], 'o?bfbtpel' ),
    ))
