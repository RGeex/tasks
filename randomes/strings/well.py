"""
В этом ката вам нужно проверить предоставленный 2-мерный массив (x) на наличие хороших идей
«хорошо» и плохих идей «плохо». Если есть одна или две хороших идеи, верните «Опубликовать!»,
если их больше 2, верните «Я чувствую серию!». Если хороших идей нет, как это часто бывает,
верните «Провал!».

Подмассивы могут иметь разную длину.

Решение не должно быть чувствительным к регистру (т.е. good, GOOD и gOOd считаются хорошей идеей).
Все входные данные не могут быть строками.
"""
import typing
import unittest


def well(arr: list[list[str]]) -> str:
    """
    Поиск хороших идей.
    """
    return {0: 'Fail!', 1: 'Publish!', 2: 'Publish!'}.get(sum(sum(x.lower() == 'good' for x in lst if isinstance(x, str)) for lst in arr), 'I smell a series!')
    


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(well, (
        ([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']], 'Fail!'),
        ([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']], 'Publish!'),
        ([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']], 'I smell a series!'),
    ))
