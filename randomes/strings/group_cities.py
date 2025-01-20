"""
Создайте функцию, которая, учитывая последовательность строк, группирует элементы, которые можно
получить путем вращения других, игнорируя верхний или нижний регистр.

В случае, если элемент встречается во входной последовательности более одного раза, для результата
будет учтен только один из них, остальные отбрасываются.
Вход

Последовательность строк. Допустимыми символами для этих строк являются символы верхнего и нижнего
регистра алфавита и пробелы.
Выход

Последовательность элементов. Каждый элемент представляет собой группу входных данных, которые
можно получить путем вращения строк.

Отсортируйте элементы каждой группы по алфавиту.

Отсортируйте группы по убыванию размера, а в случае равенства — по первому элементу группы в
алфавитном порядке.
Примеры

['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'] --> [['Kyoto', 'Okyot', 'Tokyo'],
['Donlon', 'London'], ['Paris'], ['Rome']]

['Rome', 'Rome', 'Rome', 'Donlon', 'London'] --> [['Donlon', 'London'], ['Rome']]

[] --> []
"""
import typing
import unittest


def group_cities(arr: list[str]) -> list[list[str]]:
    """
    Разделяет слова по группам.
    """
    res = {}
    for el in set(arr):
        res[x] = res.get(x := ''.join(sorted(el.lower())), []) + [el]
    return sorted([sorted(x, key=lambda x: x.lower()) for x in res.values()], key=lambda x: (-len(x), x))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(group_cities, (
        (['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'], [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]),
        (['Tokyo', 'London', 'Rome', 'Donlon'], [['Donlon', 'London'], ['Rome'], ['Tokyo']]),
        (['Rome', 'Rome', 'Rome', 'Donlon', 'London'], [['Donlon', 'London'], ['Rome']]),
        (['Ab', 'Aa'], [['Aa'], ['Ab']]),
        ([], []),
    ))
