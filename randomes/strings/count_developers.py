"""
Вам будет предоставлен массив объектов (хешей в Ruby), представляющих данные о
разработчиках, которые зарегистрировались для участия во встрече по программированию,
которую вы организуете впервые.

Ваша задача — вернуть количество разработчиков JavaScript из Европы .

Например, рассмотрим следующий список:

lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]

ваша функция должна возвращать число 1.

Если в Европе нет разработчиков JavaScript, то ваша функция должна возвращать 0.

Примечания:

    Формат строк всегда будет Europe и JavaScript.
    Все данные всегда будут достоверными и единообразными, как в примере выше.




Эта ката входит в серию Coding Meetup , которая включает в себя ряд коротких и
простых для понимания ката, разработанных для освоения использования функций
высшего порядка. В JavaScript это такие методы, как: forEach, filter, map, reduce,
some, every, find, findIndex. Конечно, возможны и другие подходы к решению ката.
"""
import typing
import unittest


def count_developers(lst: list[dict]) -> int:
    """
    Подсчитывает кол-во разработчиков JavaScript из Европы.
    """
    return sum(1 for x in lst if x.get('continent') == 'Europe' and x.get('language') == 'JavaScript')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_developers, (
            ([
                { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
                { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
                { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
                { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
            ], 1),
            ([
                { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
                { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
            ], 0),
    ))
