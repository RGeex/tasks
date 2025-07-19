"""
В скалолазании ( в частности, в боулдеринге ) уровни сложности скалолазания
V/Vermin (США) начинаются с 'VB'(самый легкий класс), а затем перейти
'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5'и т.д. до 'V17'(самый сложный класс).

Вам будет предоставлено listвосхождения на уровни, и вам нужно написать
функцию для returnа listоценок, отсортированных от самых простых к самым сложным.

Если вход пустой list, returnпустой list; в противном случае входные данные
всегда будут допустимыми listодного или нескольких классов.

Пожалуйста, голосуйте, оценивайте и оставляйте отзывы о ката.
"""
import re
import typing
import unittest


def sort_grades(lst: list[str]) -> list[str]:
    """
    Сортировка по заданному шаблону параметров.
    """
    return sorted(lst, key=lambda x: (int(re.findall(r'V(\d*)\+?', x)[-1] or -1), x))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_grades, (
        ([], []),
        (['V1'], ['V1']),
        (['V7', 'V12', 'V1'], ['V1', 'V7', 'V12']),
        (['V13', 'V14', 'VB', 'V0'], ['VB', 'V0', 'V13', 'V14']),
        (['V0+', 'V0', 'V16', 'V2', 'VB', 'V6'], ['VB', 'V0', 'V0+', 'V2', 'V6', 'V16']),
    ))
