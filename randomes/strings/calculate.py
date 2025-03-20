"""
В этой ката вы будете выполнять сложение и вычитание для заданной строки.
Возвращаемое значение также должно быть строкой.

Примечание: поле ввода не будет пустым.
Примеры

"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
"""
import typing
import unittest


def calculate(st: str) -> str:
    """
    Производит вычисления строки (сложение и вычитание).
    """
    return str(eval(st.replace('plus', '+').replace('minus', '-')))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calculate, (
        ('1plus2plus3plus4', '10'),
        ('1minus2minus3minus4', '-8'),
        ('1plus2plus3minus4', '2'),
        ('1plus2minus3plus4minus5', '-1'),
    ))
