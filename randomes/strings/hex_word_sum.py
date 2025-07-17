"""
Описание

Поскольку шестнадцатеричные значения могут включать буквы Aчерез F, некоторые
английские слова можно написать по буквам, например CAFE, BEEF, или FACADE.
Этот словарь можно расширить, используя цифры для обозначения других букв,
например 5EAF00D, или DEC0DE5.

Ваша задача — по заданной строке вернуть десятичную сумму всех слов в строке,
которые можно интерпретировать как шестнадцатеричные значения.
Пример

Работа со струной "BAG OF BEES":

"BAG"  =  0, as it is not a valid hex value  
"OF"   =  0F   =  15
"BEES" =  BEE5 =  48869

Результат равен сумме этих чисел: 48884 (0 + 15 + 48869).
Примечания

    Все входные данные вводятся заглавными буквами и не содержат знаков препинания.
    0 можно заменить O
    5 можно заменить S
"""
import typing
import unittest


def hex_word_sum(st: str) -> int:
    """
    Переводит hex в число.
    """
    return sum(int(x, 16) for x in f'0 {st}'.translate(str.maketrans('OS', '05')).split() if not set(x) - set('ABCDEF0123456789'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(hex_word_sum, (
        ('DEFACE', 14613198),
        ('SAFE', 23294),
        ('CODE', 49374),
        ('BUGS', 0),
        ('', 0),
        ('DO YOU SEE THAT BEE DRINKING DECAF COFFEE', 13565769),
        ('ASSESS ANY BAD CODE AND TRY AGAIN', 10889952),
    ))
