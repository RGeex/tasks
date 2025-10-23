"""
Слово i18n является общепринятым сокращением internationalizationв сообществе разработчиков
используется вместо того, чтобы набирать слово целиком и пытаться написать его правильно.
Сходным образом, a11yэто аббревиатура от accessibility.

Напишите функцию, которая принимает строку и преобразует все без исключения «слова» (см. ниже)
внутри этой строки длиной 4 или больше в аббревиатуру, следуя этим правилам:

    «Слово» — это последовательность букв алфавита. Согласно этому определению, любой другой символ,
    например пробел или дефис (например, «поездка на слоне»), разделит серию букв на два слова
    (например, «слон» и «поездка»).
    В сокращенном варианте слова должна быть первая буква, затем количество удаленных символов,
    затем последняя буква (например, «поездка на слоне» => «e6t r2e»).

Пример

abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"
"""
import typing
import unittest
import re


def abbreviate(s: str) -> str:
    """
    Создает из строки аббревиатуру.
    """
    return ''.join([x if len(x) < 4 else f'{len(x) - 2}'.join(x[::len(x) - 1]) for x in re.split(r'([^\W\d_]+)', s)])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(abbreviate, (
        ("internationalization", "i18n"),
        ("accessibility", "a11y"),
        ("Accessibility", "A11y"),
        ("elephant-ride", "e6t-r2e"),
    ))
