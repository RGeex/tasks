"""
Эта функция принимает список строк и помещает их в хэш-таблицу.
Хэш-таблица — это быстрый способ хранения и поиска необходимых элементов по
их хэш-значению ( https://en.wikipedia.org/wiki/Hash_table ). В этом примере
мы создадим хэши на основе суммы символов. Каждый символ имеет десятичное
значение (ASCII-код), и сумма этих десятичных значений будет хэшем.

Ваша цель — взять список строк, хешировать их и вернуть словарь с хешами в
качестве ключей и список строк с этими хешами в качестве значений.
"""
import typing
import unittest


def my_hash_map(list_of_strings: list[str]) -> dict[int, str]:
    """
    Хеширует строки.
    """
    data = {}
    for st in list_of_strings:
        hsh = sum(map(ord, st))
        data[hsh] = data.get(hsh, []) + [st]
    return data


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(my_hash_map, (
        (["alphabet"], {833: ['alphabet']}),
        (["alphabet", "black"], {833: ['alphabet'], 509:['black']}),
    ))
