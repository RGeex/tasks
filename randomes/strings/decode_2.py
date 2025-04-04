"""
Добро пожаловать в мое (удивительное) ката!

Вам дано огромное число для расшифровки. Каждое число представляет собой код, который чередуется по
шаблону между закодированным текстом и меньшим закодированным числом. Длина шаблона варьируется в
зависимости от каждого теста, но чередование между закодированным текстом и закодированным числом
будет всегда. Следуя этому правилу, каждое проверенное число начинается с закодированного текста и
заканчивается закодированным числом.
Как работает кодировка

Теперь нам, вероятно, следует рассмотреть, как формируется строка чисел, учитывая, что вам придется
ее деформировать. Итак, сначала берется и кодируется некоторый текст. Система кодирования берет позицию
каждой буквы в алфавите и добавляет к ней 100. Например, m в реальном тексте будет 113 в кодовом номере.

После текста идет двоичное число. Вам следует преобразовать это число в обычное десятичное число по
основанию 10 (все они могут быть преобразованы в целые неотрицательные числа).

Разделяя закодированный текст и закодированные числа, существует 98. Поскольку числа представлены в
двоичном формате, единственные цифры, которые они используют, — это «0» и «1», а каждая закодированная
буква алфавита находится в диапазоне от 101 до 127, все случаи 98 предназначены для обозначения разделения
между закодированным текстом и закодированными числами. Также может существовать 98 в самом конце номера.

Когда вы возвращаете окончательный ответ, текст и цифры всегда должны быть разделены запятой ( ,)
Пример

decode(103115104105123101118119981001098113113113981000) = "codewars, 18, mmm, 8"

Часть кода до первой 98 может быть декодировано в "codewars". 10010 является двоичным для 18.
113113113 переводится на "mmm". И 1000 является двоичным для 8.

Вот визуализация примера:

103 115 104 105 123 101 118 119   98   10010   98   113 113 113   98   1000
 c   o   d   e   w   a   r   s     ,     18     ,    m   m   m     ,     8
"""
import typing
import unittest


def decode(num: int) -> str:
    """
    Декодирует строку из заданного числа.
    """
    return ', '.join([str(int(x, 2)) if i % 2 else ''.join([chr(int(n) - 4) for n in f'{int(x):,}'.split(',')]) for i, x in enumerate(str(num).split('98')) if x])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(decode, (
        (103115104105123101118119981001098, 'codewars, 18'),
        (119112105105116981000981091199810019810612111498100000110001, 'sleep, 8, is, 9, fun, 2097'),
        (103115104105123101118119981001098103115104105123101118119981001098103115104105123101118119981001098, 'codewars, 18, codewars, 18, codewars, 18'),
        (120108105118105109119101112109107108120981001010101098102105108109114104125115121118105125105119981000, 'thereisalight, 1194, behindyoureyes, 8'),
    ))
