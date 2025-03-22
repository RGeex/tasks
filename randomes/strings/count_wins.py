"""
Создайте функцию, которая принимает два аргумента:

    Множество объектов, посвященных сезону, команде и стране победителя Лиги чемпионов.

    Страна (в виде строки, например, «Португалия»)

Затем ваша функция должна вернуть число, представляющее количество побед команды из данной страны.
Возврат 0если бы не было побед.

Например, если входной массив выглядит следующим образом:

countWins(winnerList1, 'Spain')=> должно вернуть 2
countWins(winnerList1, 'Portugal')=> должно вернуть 1
countWins(winnerList1, 'Sportland')=> должен вернуть 0
"""
import typing
import unittest


def count_wins(winners_list: list[dict], country: str) -> int:
    """
    Определяет кол-во побед для заданной страны.
    """
    return sum(x['country'] == country for x in winners_list)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    winner_list_1 = [
        {'season': '1996-97', 'team': 'Borussia Dortmund', 'country': 'Germany'},
        {'season': '1997-98', 'team': 'Real Madrid', 'country': 'Spain'},
        {'season': '1998-99', 'team': 'Manchester United', 'country': 'England'},
        {'season': '1999-00', 'team': 'Real Madrid', 'country': 'Spain'},
        {'season': '2000-01', 'team': 'Bayern Munich', 'country': 'Germany'},
        {'season': '2001-02', 'team': 'Real Madrid', 'country': 'Spain'},
        {'season': '2002-03', 'team': 'Milan', 'country': 'Italy'},
        {'season': '2003-04', 'team': 'Porto', 'country': 'Portugal'},
        {'season': '2004-05', 'team': 'Liverpool', 'country': 'England'},
        {'season': '2005-06', 'team': 'Barcelona', 'country': 'Spain'},
        {'season': '2006-07', 'team': 'Milan', 'country': 'Italy'},
        {'season': '2007-08', 'team': 'Manchester United', 'country': 'England'},
        {'season': '2008-09', 'team': 'Barcelona', 'country': 'Spain'},
        {'season': '2009-10', 'team': 'Internazionale', 'country': 'Italy'},
        {'season': '2010-11', 'team': 'Barcelona', 'country': 'Spain'},
        {'season': '2011-12', 'team': 'Chelsea', 'country': 'England'},
        {'season': '2012-13', 'team': 'Bayern', 'country': 'Germany'},
        {'season': '2013-14', 'team': 'Real Madrid', 'country': 'Spain'},
        {'season': '2014-15', 'team': 'Barcelona', 'country': 'Spain'},
        {'season': '2015-16', 'team': 'Real Madrid', 'country': 'Spain'}]
    test(count_wins, (
        ((winner_list_1, 'Portugal'), 1),
        ((winner_list_1, 'FootLand'), 0),
        ((winner_list_1, 'Germany'), 3),
    ))
