"""
Алан Партридж, как опытный путешественник, имеет весьма твердые взгляды на Лондон:

"Go to London. I guarantee you'll either be mugged or not appreciated.
Catch the train to London, stopping at Rejection, Disappointment,
Backstabbing Central and Shattered Dreams Parkway."

Задача

Ваша задача — проверить, что предоставленные list / array of stationsСодержит
все остановки, упомянутые Аланом. Список остановок выглядит следующим образом:

Rejection
Disappointment
Backstabbing Central
Shattered Dreams Parkway

Если все остановки появляются в заданном list / array, возвращаться Smell my
cheese you mother!, если нет, верните No, seriously, run. You will miss it..
"""
import typing
import unittest


def alan(arr: list[str]) -> str:
    """
    Проверяет что все точки указанные Аланом есть в маршруте.
    """
    points = {'Rejection','Disappointment','Backstabbing Central','Shattered Dreams Parkway'}
    return ["No, seriously, run. You will miss it.", "Smell my cheese you mother!"][points <= set(arr)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(alan, (
        (["Norwich", "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway", "London"], "Smell my cheese you mother!"),
        (["London", "Norwich"], "No, seriously, run. You will miss it."),
        (["Norwich", "Tooting", "Bank", "Rejection", "Disappointment", "Backstabbing Central", "Exeter", "Shattered Dreams Parkway", "Belgium","London"], "Smell my cheese you mother!"),
        (["London", "Norwich"], "No, seriously, run. You will miss it."),
        (["London", "Shattered Dreams Parkway", "Backstabbing Central", "Disappointment", "Rejection", "Norwich"], "Smell my cheese you mother!"),

    ))
