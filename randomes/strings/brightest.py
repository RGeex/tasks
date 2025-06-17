"""
Одним из распространенных способов представления цвета является цветовая модель RGB,
в которой основные цвета света — красный, зеленый и синий — складываются различными
способами для воспроизведения широкого спектра цветов.

Одним из способов определения яркости цвета является нахождение значения V альтернативной
цветовой модели HSV (Hue, Saturation, Value). Значение определяется как наибольший компонент цвета:

V = max(R,G,B)

Вам дан список цветов в 6-значной шестнадцатеричной системе счисления. #RRGGBB.
Верните самые яркие из этих цветов!

Например,

brightest(["#001000", "#000000"]) == "#001000"
brightest(["#ABCDEF", "#123456"]) == "#ABCDEF"

Если самых ярких цветов несколько, вернуть первый:

brightest(["#00FF00", "#FFFF00", "#01130F"]) == "#00FF00"

Обратите внимание, что как на входе, так и на выходе следует использовать заглавные
символы. A, B, C, D, E, F.
"""
import typing
import unittest


def brightest(colors: list[str]) -> str:
    """
    Поиск самого яркого цвета.
    """
    return max(colors, key=lambda x: max(int(x[i:i + 2], 16) for i in range(1, 7, 2)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(brightest, (
        (["#001000", "#000000"], "#001000"),
        (["#ABCDEF", "#123456"], "#ABCDEF"),
        (["#00FF00", "#FFFF00"], "#00FF00"),
        (["#FFFFFF", "#1234FF"], "#FFFFFF"),
        (["#FFFFFF", "#123456", "#000000"], "#FFFFFF"),
    ))
