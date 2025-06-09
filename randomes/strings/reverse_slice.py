"""
Вам будет предоставлена ​​строка символов в качестве входных данных. Завершите функцию,
которая возвращает список строк: (а) в обратном порядке исходной строки, и (б) каждая
последующая строка начинается на один символ дальше от конца исходной строки.

Предположим, что исходная строка имеет длину не менее 3 символов. Попробуйте сделать
это с помощью срезов и избегайте преобразования строки в список.
Примеры

'123'   ==>  ['321', '21', '1']
'abcde' ==>  ['edcba', 'dcba', 'cba', 'ba', 'a']
"""
import typing
import unittest


def reverse_slice(st: str) -> list[str]:
    """
    Создает из строки список стор в обратном порядске с уменьшением символов.
    """
    return [st[::-1][i:] for i in range(len(st))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_slice, (
        ('123', ['321', '21', '1']),
        ('abcde', ['edcba', 'dcba', 'cba', 'ba', 'a']),
    ))
