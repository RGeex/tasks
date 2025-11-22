"""
Задача
Учитывая длину, смещение и список, перемещаем окно этой длины,
перемещаясь на это смещение каждый шаг, по списку, возвращая список списков.

Окна могут перекрывать друг друга или пропускать некоторые элементы.
Все окна должны иметь заданную длину; если после определённого смещения
остаётся недостаточно элементов, список списков завершается. Можно брать
элементы 0из пустого списка, поэтому будьте внимательны и корректны window(0,offset,list).

Длина всегда будет неотрицательной; смещение всегда будет строго положительным.

Примеры
for 2, 1, [0,1,2,3,4] return [ [0,1], [1,2], [2,3], [3,4] ]
for 2, 2, [0,1,2,3,4] return [ [0,1], [2,3] ]
for 2, 3, [0,1,2,3,4] return [ [0,1], [3,4] ]
"""
import typing
import unittest


def window(lngth: int, offst: int, lst: list[int]) -> list[list[int]]:
    """
    Создает список сипсков элементов последовательности заданного шага и длины.
    """
    return [lst[i:i + lngth] for i in range(0, len(lst) - lngth + 1, offst)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(window, (
        ((2, 1, [0, 1, 2, 3, 4]), [[0, 1], [1, 2], [2, 3], [3, 4]]),
        ((2, 2, [0, 1, 2, 3, 4]), [[0, 1], [2, 3]]),
        ((2, 3, [0, 1, 2, 3, 4]), [[0, 1], [3, 4]]),
        ((3, 1, [0, 1, 2]), [[0, 1, 2]]),
        ((2, 1, [0, 1, 2]), [[0, 1], [1, 2]]),
        ((1, 1, [0, 1, 2]), [[0], [1], [2]]),
        ((0, 1, [0, 1, 2]), [[], [], [], []]),
    ))
