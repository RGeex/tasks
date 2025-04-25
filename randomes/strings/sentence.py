"""
Входными данными будет массив словарей.

Возвращает значения в виде предложения, разделенного строками, в порядке целочисленного
эквивалента их ключей (по возрастанию).

Ключи не повторяются и их диапазон -999 < key < 999. Ключи и значения словарей всегда
будут строками и не будут пустыми.
Пример

Input:
List = [
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]

Output:
'Vatsan took his dog for a spin'
"""
import typing
import unittest
from functools import reduce


def sentence(lst: list[dict]) -> str:
    """
    Создание строки из списка словарей, отсортированных по числовым значениям ключей.
    """
    return ' '.join(dict(sorted(reduce(lambda a, b: a | b, lst).items(), key=lambda x: int(x[0]))).values())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sentence, (
        ([{'1': 'dog'}, {'2': 'took'}, {'4': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}], 'dog took Vatsan for a spin'),
        ([{'3': 'Jake.'}, {'5': 'Chinatown'}, {'1': 'Forget'}, {'4': 'It is'}, {'2': 'it'}], 'Forget it Jake. It is Chinatown'),
        ([{'3': 'vatsan!'}, {'2': 'love'}, {'1': 'I'}], 'I love vatsan!'),
        ([{'0': 'Wars'}, {'-1': 'Code'}], 'Code Wars'),
    ))
