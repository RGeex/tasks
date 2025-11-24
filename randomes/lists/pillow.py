"""
Как сообщается, «День «Положи подушку на холодильник» отмечается ежегодно 29 мая в Европе и США.
Этот день посвящен процветанию, удаче и веселью».

Мне все это кажется очень странным.

Тем не менее, вам будет предоставлен массив из двух строк (строок). Сначала выясните,
содержит ли первая строка холодильник... (я решил, что это «n», так как похоже,
что там что-то может храниться).

Затем проверьте, есть ли во второй строке подушка — считается «B»
(не удалось добиться очевидного характера подушки).

Если подушка лежит на холодильнике — должно быть, 29 мая! Или какой-то странный дом...
Верните значение true; Для ясности, «наверху» означает прямо сверху, то есть в той же индексной позиции.

Если подушка находится где-то еще в «доме», вернуть false;

Холодильников может быть несколько, как и подушек. Но для возврата результата «истина»
необходимо, чтобы на холодильнике лежала хотя бы одна подушка. Наличие нескольких
подушек на холодильнике также должно возвращать результат «истина».
"""
import typing
import unittest


def pillow(arr: list[str]) -> bool:
    """
    Определяет, находится ли подушка на холодильнике.
    """
    return not next((0 for a, b in zip(*arr) if a + b == 'nB'), 1)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(pillow, (
        (['EvH/KNikBiyxfeyK/miCMj', 'I/HwjnHlFLlahMOKNadps'], False),
        (['\\DjQ\\[zv]SpG]Z/[Qm\\eLL', 'amwZArsaGRmibriXBgTRZp'], False),
        ([ 'n', 'B' ], True),
        (['yF[CeAAiNihWEmKxJc/NRMVn', 'rMeIa\\KAfbjuLiTnAQxNw[XB'], True),
        (['inECnBMAA/u', 'ABAaIUOUx/M'], True),
    ))
