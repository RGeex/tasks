"""
Даны строка и массив индексов. Переставьте символы строки так,
чтобы каждый символ оказался в позиции, указанной соответствующим индексом в массиве.
Примеры

Вход : 'abcd', [0, 3, 1, 2]

Выход : 'acdb'

Объяснение:

    Персонаж 'a'находится в индексе 0.

    Персонаж 'b'находится в индексе 3.

    Персонаж 'c'находится в индексе 1.

    Персонаж 'd'находится в индексе 2.

Примечания

    Строка и массив всегда будут иметь одинаковую длину.

    И строка, и массив будут содержать допустимые символы (AZ, az или 0-9).



"""
import typing
import unittest


def scramble(st: str, arr: list[int]) -> str:
    """
    Сортирует строку по заданному порядку индексов.
    """
    return ''.join(dict(sorted(zip(arr, st))).values())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(scramble, (
        (('abcd', [0,3,1,2]), 'acdb'),
        (('sc301s', [4,0,3,1,5,2]), "c0s3s1"),
        (('bskl5', [2,1,4,3,0]), "5sblk"),
    ))
