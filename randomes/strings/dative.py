"""
Гармония гласных — явление в некоторых языках. Это означает, что «гласная или гласные в
слове изменяются, чтобы звучать одинаково (таким образом, «гармонично»)» ( википедия ).
Эта ката основана на гармонии гласных в венгерском языке .
Задача:

Ваша цель — создать функцию dative()( Dative()в C#), который возвращает допустимую форму
допустимого венгерского слова wв дательном падеже , т.е. добавить правильный суффикс nek
или nakк слову wосновано на правилах гармонии гласных.
Правила гармонии гласных (упрощенные)

Когда последняя гласная в слове

    гласный переднего ряда ( e, é, i, í, ö, ő, ü, ű) суффикс -nek
    гласный заднего ряда ( a, á, o, ó, u, ú) суффикс -nak

Примеры:

dative("ablak") == "ablaknak"
dative("szék") == "széknek"
dative("otthon") == "otthonnak"

Предпосылки:

    Если говорить просто: все слова заканчиваются на согласную :)
    Все строки являются строками Unicode.
    В тестах нет грамматических исключений.
"""
import typing
import unittest


def dative(word: str) -> str:
    """
    Создание правильного окончания венгерского слова.
    """
    a, b = 'eéiíöőüű', 'aáoóuú'
    return word + next(f'n{"ae"[x in a]}k' for x in word[::-1] if x in a + b)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(dative, (
        ("ablak", "ablaknak"),
        ("tükör", "tükörnek"),
        ("keret", "keretnek"),
        ("otthon", "otthonnak"),
        ("virág", "virágnak"),
        ("tett", "tettnek"),
        ("rokkant", "rokkantnak"),
        ("rossz", "rossznak"),
        ("gonosz", "gonosznak"),
        ("rög", "rögnek"),
        ("király", "királynak"),
    ))
