"""
Covfefe

Вам дают строку. Вы должны заменить любое событие последовательности coverage к covfefe,
однако, если вы не найдете слово coverage В строке вы должны добавить covfefe В конце
струны с ведущим пространством.
"""
import typing
import unittest


def covfefe(st: str) -> str:
    """
    Заменяет слова в строке, в случае отсутствия заданного слова, добавляет слово замену в конец строки.
    """
    return (res := st.replace('coverage', 'covfefe')) + ['', ' covfefe'][res == st]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(covfefe, (
        ("coverage","covfefe"),
        ("coverage coverage","covfefe covfefe"),
        ("nothing","nothing covfefe"),
        ("double space ","double space  covfefe"),
        ("covfefe","covfefe covfefe"),
        ("erag","erag covfefe"),
    ))
