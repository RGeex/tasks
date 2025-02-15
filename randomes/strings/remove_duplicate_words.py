"""
Ваша задача состоит в том, чтобы удалить все дубликаты из строки, оставляя только одиночные (первые) записи слова.

Пример:

Вход:

'Альфа -бета -бета -гамма гамма гамма дельта Альфа Бета Бета Гамма Гамма Гамма Дельта'

Выход:

'Alpha Beta Gamma Delta'
"""
import typing
import unittest


def remove_duplicate_words(st: str) -> str:
    """
    Удаляет из строки дубликаты, сохраняя порядок слов.
    """
    return ' '.join({word: 0 for word in st.split()}.keys())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_duplicate_words, (
        ("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta", "alpha beta gamma delta"),
        ("my cat is my cat fat", "my cat is fat"),

    ))
