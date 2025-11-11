"""
Учитывая массив мест, вернуть максимальное количество новых людей,
которых можно посадить, при условии, что между людьми останется не менее 2 мест .

Свободные места указаны как 0.
Занятые места указаны как 1.
Не перемещайте уже занятые места, даже если они находятся на расстоянии менее
двух друг от друга. Учитывайте только расстояние между новыми и уже существующими местами.
Примеры
[0, 0, 0, 1, 0, 0, 1, 0, 0, 0] ➞ 2
// [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

[0, 0, 0, 0] ➞ 2
// [1, 0, 0, 1]

[1, 0, 0, 0, 0, 1] ➞ 0
// There is no way to have a gap of at least 2 chairs when adding someone else.
Примечания
Обратите внимание, что может быть несколько возможностей распределения мест среди людей,
но эти случаи не повлияют на результаты.
Все места будут действительны.
"""
import typing
import unittest


def maximum_seating(lst: list[int]) -> int:
    """
    Определяет какое кол-во людей можно посадить в зал, так что бы между сидячими был промежуток в места.
    """
    res = 0
    for i, n in enumerate(lst):
        if not n and not sum(lst[i > 2 and i - 2:i]) and not sum(lst[i + 1:i + 3]):
            lst[i], res = 1, res + 1
    return res


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(maximum_seating, (
        ([0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 2),
        ([0, 0, 0, 0], 2),
        ([1, 0, 0, 0, 0, 0, 1], 1),
        ([1, 0, 0, 0, 0, 0, 0, 1], 1),
        ([1, 0, 0, 0, 0, 1], 0),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 4),
        ([0], 1),
        ([0, 0], 1),
        ([1], 0),
        ([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0], 1),
    ))
