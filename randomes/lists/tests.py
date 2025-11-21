"""
Сегодня важный день: в классе только что закончился контрольная по математике.
Вам выдадут список оценок. Выполните функцию, которая:

Рассчитайте средний балл всего класса и округлите его до трех знаков после
запятой.
Создайте словарь/хэш с ключами "h", "a", "l", чтобы было понятно, сколько
оценок high, average и low они получили. Высокие оценки — 9 и 10,
средние — 7 и 8, а низкие — от 1 до 6.
Верните список, [class_average, dictionary]если есть разные типы оценок или
[class_average, dictionary, "They did well"]только высокие оценки.
Примеры
[10, 9, 9, 10, 9, 10, 9] ==> [9.429, {'h': 7, 'a': 0, 'l': 0}, 'They did well']

[5, 6, 4, 8, 9, 8, 9, 10, 10, 10] ==> [7.9, {'h': 5, 'a': 2, 'l': 3}]
"""
import typing
import unittest


def tests(arr: list[int]) -> list[float, dict[str, int], str]:
    """
    Вычисляет статистические данные по аданному условию.
    """
    res, tmp, data = 0, set('hal'), dict.fromkeys('hal', 0)
    for n in arr:
        x = next('hal'[i] for i, x in enumerate((8, 6, 0)) if n > x)
        res, tmp, data[x] = res + n, tmp - set(x), data.get(x) + 1
    return [round(res / len(arr), 3), data, 'They did well'][:2 + (tmp == set('al'))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(tests, (
        ([10,9,9,10,9,10,9],[9.429, {'h': 7, 'a': 0, 'l': 0}, 'They did well']),
        ([5,6,4,8,9,8,9,10,10,10],[7.9, {'h': 5, 'a': 2, 'l': 3}]),
        ([5,6,5,7,4,5,6,6,5],[5.444, {'h': 0, 'a': 1, 'l': 8}]),
        ([9,8,7,6,9,8,10,7,6],[7.778, {'h': 3, 'a': 4, 'l': 2}]),
        ([9,10,10,10,10,10,8,9,7,8,10],[9.182, {'h': 8, 'a': 3, 'l': 0}]),
        ([3,5,6,10,8,4,10,9],[6.875, {'h': 3, 'a': 1, 'l': 4}]),
        ([10,9,9,10,9,10],[9.5, {'h': 6, 'a': 0, 'l': 0}, 'They did well']),
        ([7,6,8,9,6,7,5,9],[7.125, {'h': 2, 'a': 3, 'l': 3}]),
        ([9,9,8,9,8,9],[8.667, {'h': 4, 'a': 2, 'l': 0}]),
        ([10,9,6,7,10,8,9,10],[8.625, {'h': 5, 'a': 2, 'l': 1}]),
    ))
