"""
Вам дан начальный массив из 2 значений (x). Вы будете использовать его для расчета баллов.

Если оба значения в (x) являются числами, оценка равна сумме двух. Если только одно из них является
числом, оценка равна этому числу. Если ни одно из них не является числом, вернуть «Void!».

Получив оценку, вы должны вернуть массив массивов. Каждый подмассив будет таким же, как (x),
а количество подмассивов должно быть равно оценке.

Например:

если (x) == ['a', 3], вы должны вернуть [['a', 3], ['a', 3], ['a', 3]].

"""
import typing
import unittest


def explode(arr: list[int|str]) -> list[list[int|str]]:
    """
    Выполняет оценку по заданному критерию.
    """
    return [[arr] * sum(x := [x for x in arr if isinstance(x, int)]), 'Void!'][not x]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(explode, (
        ([9, 3], [[9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3]]),
        (['a', 3], [['a', 3], ['a', 3], ['a', 3]] ) ,
        ([6, 'c'], [[6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c']]) ,
        (['a', 'b'], 'Void!') ,
        ([1, 0], [[1,0]]) ,
        (["a", 0], []),
    ))
