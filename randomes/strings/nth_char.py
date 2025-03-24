"""
Завершите функцию, которая принимает массив слов.

Вы должны объединить n-я буква из каждого слова, чтобы построить новое слово,
которое должно быть возвращено в виде строки, где n— позиция слова в списке.

Например:

["yoda", "best", "has"]  -->  "yes"
  ^        ^        ^
  n=0     n=1     n=2

Примечание: Тестовые случаи содержат только допустимые входные данные, т. е.
массив строк или пустой массив; и каждое слово будет иметь достаточное количество букв.
"""
import typing
import unittest


def nth_char(words: list[str]) -> str:
    """
    Составляет слово, взяв по 1 букве из каждого слова списка согласно индексу слова.
    """
    return ''.join(word[i] for i, word in enumerate(words))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(nth_char, (
        (['yoda', 'best', 'has'], 'yes'),
        ([],''),
        (['X-ray'],'X'),
        (['No','No'],'No'),
        (['Chad','Morocco','India','Algeria','Botswana','Bahamas','Ecuador','Micronesia'],'Codewars'),
    ))
