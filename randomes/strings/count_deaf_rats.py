"""
История

Крысолов был призван сыграть свою волшебную мелодию и выманить всех крыс из
города.

Но некоторые крысы глухие и идут не туда!
Ката Задача

Сколько здесь глухих крыс?
Легенда

    P = Крысолов
    O~ = Крыса идет налево
    ~O = Крыса идет направо

Пример

    ex1 ~O~O~O~O P имеет 0 глухих крыс

    ex2 P O~ O~ ~O O~ есть 1 глухая крыса

    ex3 ~O~O~O~OP~O~OO~ есть 2 глухие крысы

"""
import typing
import unittest


def count_deaf_rats(s: str):
    """
    Вычисляет кол-во глухих крыс.
    """
    return sum([x[i*2:i*2+2] for i in range(len(x)//2)].count('~O'[::[-1, 1][i]]) for i, x in enumerate(s.replace(' ', '').split('P')))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_deaf_rats, (
        ("~O~O~O~O P", 0),
        ("P O~ O~ ~O O~", 1),
        ("~O~O~O~OP~O~OO~", 2),
    ))
