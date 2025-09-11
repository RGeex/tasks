"""
Майк и Джо — члены студенческого братства, которые обожают пиво и игры,
связанные с выпивкой. Они играют в следующую игру: Майк выпивает одно пиво,
Джо — два, Майк — три, Джо — четыре и так далее. Если кто-то не может выпить
положенное количество пива, он проигрывает.

Майк может выпить максимум A бутылок пива за раз (иначе он потеряет сознание),
а Джо — максимум B бутылок пива за раз. Кто победит в игре?

Напишите функцию game(A,B)который возвращает победителя, "Mike" или
"Joe"соответственно, для любых заданных целых значений A и B.

Примечание: если Майк или Джо не могут выпить хотя бы одну кружку пива,
верните строку "Non-drinkers can't play".
"""
import typing
import unittest


def game(a: int, b: int) -> str:
    """
    Определяет победителя в игре кто больше выпьет.
    """
    return ['Mike', 'Joe'][(c := int(a ** 0.5)) * (c + 1) <= b] if a * b else "Non-drinkers can't play"

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(game, (
        ((3,2), "Joe"),
        ((4,2), "Mike"),
        ((9,1000), "Joe"),
        ((0,1), "Non-drinkers can't play"),
    ))
