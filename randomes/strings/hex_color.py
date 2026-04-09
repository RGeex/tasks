"""
Вы просматриваете различные шестнадцатеричные коды и испытываете трудности с
определением разницы между #000001 и #100000.

Нам нужен способ определить, где красный, а где синий!

Вот где вы создаёте шестнадцатеричный код цвета !!!

Программа должна считывать RGB-сигнал и возвращать то значение (красный, синий или зеленый),
которое соответствует наибольшей концентрации!

Но если концентрация нескольких цветов одинакова, вам следует вернуть эту смесь!

red + blue = magenta

green + red = yellow

blue + green = cyan

red + blue + green = white

И ещё одно: если переданная строка пуста или состоит из одних нулей, верните black!

Примеры:

codes = "087 255 054" -> "green"
codes = "181 181 170" -> "yellow"
codes = "000 000 000" -> "black"
codes = "001 001 001" -> "white"

"""
import unittest
from typing import Any, Callable, Tuple


def hex_color(codes: str) -> str:
    """
    Определяет цвет из RGB сигнала.
    """
    data, colors = {}, {(0,): 'red', (1,): 'green', (2,): 'blue', (0, 1): 'yellow', (0, 2): 'magenta', (1, 2): 'cyan', (0, 1, 2): 'white'}
    for i, x in enumerate(codes.split()):
        if int(x):
            data[x] = data.get(x, []) + [i]
    return colors.get(tuple(max(data.items(), default=(0, [3]))[1]), 'black')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(hex_color, (
        ('', 'black'),
        ('000 000 000', 'black'),
        ('121 245 255', 'blue'),
        ('027 100 100', 'cyan'),
        ('021 021 021', 'white'),
        ('255 000 000', 'red'),
        ('000 147 000', 'green'),
        ('212 103 212', 'magenta'),
        ('101 101 092', 'yellow'),
    ))
