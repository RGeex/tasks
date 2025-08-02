"""
Счастливых праздников, товарищи Воины Кода!

Старший организатор подарков Санты Эльф разработал способ обозначения до 26
подарков, присвоив каждому из них уникальный алфавитный символ. После того,
как каждому подарку был назначен символ, организатор подарков Эльф объединил
символы, чтобы сформировать код заказа подарка.

Санта попросил своего организатора расставить персонажей в алфавитном порядке,
но эльф уснул, съев слишком много горячего шоколада и леденцов! Помогите ему!
Сортировать подарочный код

Напишите функцию под названием sortGiftCode/ sort_gift_code/ SortGiftCodeкоторый
принимает строку, содержащую до 26 уникальных алфавитных символов, и возвращает
строку, содержащую те же символы в алфавитном порядке.
Примеры (Вход -- => Выход):

"abcdef"                      -- => "abcdef"
"pqksuvy"                     -- => "kpqsuvy"
"zyxwvutsrqponmlkjihgfedcba"  -- => "abcdefghijklmnopqrstuvwxyz"
"""
import typing
import unittest


def sort_gift_code(code: str) -> str:
    """
    Сортирует символы строки в алфавитном порядке.
    """
    return ''.join(sorted(code))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_gift_code, (
        ('abcdef', 'abcdef'),
        ('pqksuvy', 'kpqsuvy'),
        ('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz'),
    ))
