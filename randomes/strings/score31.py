"""
Задача

Ваша цель — узнать счёт руки, получив три карты одного достоинства или
одной масти. Стоимость руки рассчитывается путём сложения всех карт одной
масти .

Обычные карты стоят по своему номиналу, карты с картинками стоят 10,
а тузы — 11, но помните, учитывается только одна ваша масть !

Вы также можете собрать руку из трёх карт одного ранга , например,
8-8-8 или JJJ. Такая комбинация приносит 30,5 очков, за исключением AAA,
которая приносит 32 очка.

Возьмите три строки: c1, c2 и c3 и верните числовое значение score .
Примеры

score31("CA", "D9", "H8") ➞ 11
# CA = 11
# D9 = 9
# H8 = 8
# Return max score = 11

score31("SJ", "SQ", "S8") ➞ 28
# SJ + SQ + S8 = 10 + 10 + 8 = 28

score31("DA", "DK", "DQ") ➞ 31
# DA + DK + DQ = 11 + 10 + 10 = 31

score31("S9", "C9", "H9") ➞ 30.5
# Same numbers = 30.5

score31("SA", "CA", "HA") ➞ 32
# All A's = 32

Примечания

    Карты бывают следующих мастей: H-hearts, C-clubs, S-spades, and D-diamonds
    Цифры: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A


"""
import typing
import unittest


def score31(c1: str, c2: str, c3: str) -> int | float:
    """
    Определяет стоимость комбинации карт.
    """
    data = {}
    for x in (c1, c2, c3):
        data[x[0]] = data.get(x[0], []) + [x[1:] in 'JQKA' and [10, 11][x[1:] == 'A'] or int(x[1:])]
    return len(set(x := list(map(sum, data.values())))) == 1 and len(x) == 3 and [30.5, 32][x[-1] == 11] or max(x)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(score31, (
        (('CA','D9','H8'), 11),
        (('SJ','SQ','S8'), 28),
        (('DA','DK','DQ'), 31),
        (('SK','CK','HK'), 30.5),
        (('SA','CA','DA'), 32),
        (('SJ','H9','CJ'), 10),
        (('SA','CA','C10'), 21),
        (('SJ','SQ','DK'), 20),
        (('D7','D8','D10'), 25),
        (('CJ','CQ','CA'), 31),
        (('SK','CK','HK'), 30.5),
        (('CA','SA','HA'), 32),
        (('C10','S10','H10'), 30.5),
    ))
