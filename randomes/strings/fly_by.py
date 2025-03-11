"""
На днях я увидел удивительное видео, в котором парень взломал некоторых лампочек,
контролируемых Wi -Fi, проехав мимо их беспилотника. Блестящий.

В этом kata мы воссоздаем этот трюк ... вроде.

Вам дадут две строки: lamps и drone. lamps представляет ряд ламп, в настоящее время
выключенные, каждая из которых представлен xПолем Когда эти лампы включены, они
должны быть представлены o.

А drone строка представляет положение беспилотника T (Любое лучшее предложение
для персонажа ??) и его трасса полета до этого момента =Полем Дрон всегда летает
слева направо и всегда начинается в начале ряда ламп. В любом месте пролетал
беспилотник, включая его текущее положение, приведет к тому, что лампа в этом
положении включается.

Вернуть полученное lamps нить. Смотрите примеры тестов для большей ясности.
"""
import typing
import unittest


def fly_by(lamps: str, drone: str) -> str:
    """
    Переключени ламп при приближении дрона.
    """
    return lamps.replace('x', 'o', len(drone))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(fly_by, (
        (('xxxxxx', '====T'), 'ooooox'),
        (('xxxxxxxxx', '==T'), 'oooxxxxxx'),
        (('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx'),
    ))
