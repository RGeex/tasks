"""
Ваша задача очень проста. Просто напишите функцию, которая принимает на вход строку строчных букв
и возвращает true/ falseв зависимости от того, расположена ли строка в алфавитном порядке или нет.
Примеры (вход -> выход)

    "kata" -> false ('a' идет после 'k')
    "ant" -> true (все символы в алфавитном порядке)

"""
import typing
import unittest


def alphabetic(st: str) -> bool:
    """
    Проверяет, расположены ли буквы в строке в алфавитном порядке.
    """
    return sorted(st) == list(st)
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(alphabetic, (
        ('asd', False),
        ('codewars', False),
        ('door', True),
        ('cell', True),
        ('z', True),
        ('', True),
    ))
