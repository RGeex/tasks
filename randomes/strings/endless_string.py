"""
Создайте функцию, которая принимает 3 входа, строку, начальное местоположение и длину.
Функция должна имитировать строку бесконечно повторять в обоих направлениях и возвращать
подстроение, начинающееся в начальном месте, и продолжается для длины.

Пример:

endless_string('xyz', -23, 6) == 'yzxyzx'

Чтобы визуализировать:

       Negative                               Positive
3         2         1         *         1         2         3
0987654321098765432109876543210123456789012345678901234567890
xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzx
       ******
     -23 for a length of 6 == 'yzxyzx'


Еще несколько примеров:

endless_string('xyz', 0, 4) == 'xyzx'
endless_string('xyz', 19, 2) == 'yz'
endless_string('xyz', -4, -4) == 'zxyz'

Негативная длина должна включать начальную позицию и вернуть символы слева от исходной позиции.
"""
import typing
import unittest


def endless_string(seq: str, start: int, length: int) -> str:
    """
    Возвращает подстроение, начинающееся в начальном месте, и продолжается для длины.
    """
    k, n = [x := start % len(seq), len(seq) - x - 1][length < 0], not length or length // abs(length)
    return ''.join([seq[::n][(k + i) % len(seq)] for i in range(abs(length))])[::n]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(endless_string, (
        (('xyz', -23, 6), 'yzxyzx'),
        (('xyz', 0, 4), 'xyzx'),
        (('xyz', 19, 2), 'yz'),
        (('xyz', -4, -4), 'zxyz'),
    ))
