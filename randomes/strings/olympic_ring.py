"""
В честь начала Олимпиады в Рио (и возвращения «Последнего этапа» на C4 сегодня вечером)
мы представляем ката, вдохновленное Олимпийскими играми.

Вам дана строка случайных букв, и вам нужно изучить каждую из них. Некоторые буквы естественным
образом имеют «кольца». «O» — очевидный пример, но «b», «p», «e», «A» и т. д. также применимы.
«B» имеет даже два!! Обратите внимание, что для этого ката вы можете считать строчную «g» только
одним кольцом.

Ваша задача — посчитать «кольца» в каждой букве и разделить общее число на 2. Округлите ответ в
меньшую сторону. Когда у вас будет окончательный счет:

если оценка равна 1 или меньше, вернуть «Даже медали нет!»; если оценка равна 2, вернуть «Бронза!»;
если оценка равна 3, вернуть «Серебро!»; если оценка больше 3, вернуть «Золото!»;

Точки над буквами i и любыми другими буквами кольцами не считаются.

"""
import re
import typing
import unittest


def olympic_ring(st: str) -> str:
    """
    Определяет место по кл-ву колец в буквах в строке.
    """
    n = ((b := (x := re.sub(r'[^ABDOPQRabdegopq]', '', st)).count('B')) * 2 + (len(x) - b)) // 2
    return {n < 2: 'Not even a medal!', n == 2: 'Bronze!', n == 3: 'Silver!', n > 3: 'Gold!'}.get(1)



def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(olympic_ring, (
        ('wHjMudLwtoPGocnJ', 'Bronze!'),
        ('eCEHWEPwwnvzMicyaRjk', 'Bronze!'),
        ('JKniLfLW', 'Not even a medal!'),
        ('EWlZlDFsEIBufsalqof', 'Silver!'),
        ('IMBAWejlGRTDWetPS', 'Gold!'),
    ))
