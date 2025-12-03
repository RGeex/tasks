"""
Просто найдите в списке ближайшее к нулю значение. Обратите внимание,
что в списке есть отрицательные числа.

Список всегда непустой и содержит только целые числа. Возврат Noneесли
невозможно определить только одно из таких значений. И, конечно же, мы
ожидаем 0 как ближайшее к нулю значение.

Примеры:

[2, 4, -1, -3]  => -1
[5, 2, -2]      => None
[5, 2, 2]       => 2
[13, 0, -6]     => 0


"""
import typing
import unittest


def closest(lst: list[int]) -> int:
    """
    Поиск ближайшего к 0 числа, если нет конкурентов.
    """
    return None if (n := min(lst, key=abs)) and -n in lst else n


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(closest, (
        ([10, 3, 9, 1], 1),
        ([2, 4, -1, -3], -1),
        ([5, 2, -2], None),
        ([5, 2, 2], 2),
        ([13, 0, -6], 0),
        ([1], 1),
    ))
