"""
Поиск своего места в самолете никогда не доставляет удовольствия, особенно во время дальних
перелетов... Вы прилетаете, снова понимаете, как мало у вас места для ног, и забираетесь на
сиденье, заваленное кучей собственных вещей.

Чтобы еще больше запутать ситуацию (хотя они утверждают, что пытаются сделать наоборот),
многие авиакомпании исключают буквы «I» и «J» из своей системы наименования мест.

Система наименования состоит из числа (в данном случае от 1 до 60), которое обозначает секцию
самолета, где находится сиденье (1-20 = спереди, 21-40 = посередине, 41-60 = сзади). За этим
числом следует буква AK с исключениями, упомянутыми выше.

Буквы AC обозначают места в левом кластере, DF — в среднем, а GK — в правом.

Зная номер места, ваша задача — вернуть местоположение места в следующем формате:

«2B» вернет «Front-Left».

Если число больше 60 или буква недействительна, верните «Нет места!!».

"""
import typing
import unittest
from itertools import starmap


def plane_seat(st: str) -> str:
    """
    Определяет положение места в самолете, согласно билету.
    """
    posx = dict(zip(('Front', 'Middle', 'Back'), starmap(range, zip((x := range(1, 62, 20)), x[1:]))))
    posy = dict(zip(('Left', 'Middle', 'Right'), 'ABC DEF GHK'.split()))
    resx, resy = [next((a for a, b in dct.items() if val in b), 0) for dct, val in ((posx, int(st[:-1])), (posy, st[-1]))]
    return resx and resy and '-'.join((resx, resy)) or 'No Seat!!'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(plane_seat, (
        ('2B', 'Front-Left'),
        ('20B', 'Front-Left'),
        ('58I', 'No Seat!!'),
        ('60D', 'Back-Middle'),
        ('17K', 'Front-Right'),
    ))
