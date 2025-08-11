"""
В генетических алгоритмах кроссинговер — это генетический оператор,
используемый для изменения программирования хромосом от одного поколения к другому.

Одноточечный кроссинговер заключается в обмене участками одной хромосомы с
другой в заданной точке. На изображении ниже показано применение кроссинговера к
хромосомам. 1011011001111 и 1011100100110с точкой отсечения (индекс) 4:

В этом ката вам нужно реализовать функцию, которая получает две хромосомы.
chromosome1, chromosome2и нулевой отсчет indexи он должен вернуть массив с
результатами кроссинговера на обеих хромосомах [chromosome1, chromosome2].
Пример:

chromosome1 = "111000"
chromosome2 = "000110"
index = 3
# should return ["111110", "000000"]

"""
import typing
import unittest


def crossover(chromosome1: str, chromosome2: str, index: int) -> list[str]:
    """
    Обменивает участки 2-х хромосом.
    """
    return list(map(''.join, zip(*[x[::i < index or -1] for i, x in enumerate(zip(chromosome1, chromosome2))]))) or ['', '']


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(crossover, (
        (("110", "001", 2), ["111", "000"]),
        (("111000", "000110", 3), ["111110", "000000"]),
    ))
