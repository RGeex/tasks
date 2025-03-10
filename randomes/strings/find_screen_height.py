"""
Сырьи чизман только что получил новый монитор! Он доволен этим, но он только что обнаружил,
что его старые обои на рабочем столе больше не подходят. Он хочет найти новые обои, но не знает,
какой размер обои он должен искать, и, увы, он просто выбросил коробку нового монитора. К счастью,
он помнит ширину и соотношение сторон монитора, когда Боб Мортимер продал его ему.
Вы можете помочь ухонуть?
Задача

Учитывая целое число width и строка ratio написано как WIDTH:HEIGHT, выводате размеры экрана как
строка, написанная как WIDTHxHEIGHT.

ПРИМЕЧАНИЕ. Расчетная высота должна быть представлена ​​в качестве целого числа. Если высота
дробная, усечь ее.
"""
import typing
import unittest


def find_screen_height(width: int, ratio: str) -> str:
    """
    По заданной ширене и соотношению сторон монитора, выводит расширение.
    """
    return '%dx%d' % (width, int(eval(f'{width}/{ratio.replace(":", "*")}')))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_screen_height, (
        ((1024, "4:3"), "1024x768"),
        ((1280, "16:9"), "1280x720"),
        ((3840, "32:9"), "3840x1080"),
        ((1600, "4:3"), "1600x1200"),
        ((1280, "5:4"), "1280x1024"),
        ((2160, "3:2"), "2160x1440"),
        ((1920, "16:9"), "1920x1080"),
        ((5120, "32:9"), "5120x1440"),
    ))
