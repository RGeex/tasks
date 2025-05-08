"""
Изограмма — это слово, в котором нет повторяющихся букв, последовательных или непоследовательных.
Реализуйте функцию, которая определяет, является ли строка, содержащая только буквы, изограммой.
Предположим, что пустая строка — изограмма. Игнорировать регистр букв.

Пример: (Вход -> Выход)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)


"""
import typing
import unittest


def is_isogram(st: str) -> bool:
    """
    Проверяет является ли слово изограммой.
    """
    return len(st.lower()) == len(set(st.lower()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_isogram, (
        ("Dermatoglyphics", True),
        ("isogram", True),
        ("aba", False),
        ("moOse", False),
        ("isIsogram", False),
        ("", True),
    ))
