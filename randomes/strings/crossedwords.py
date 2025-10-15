"""
Перекрещенные слова

Это забавная Ката для любителей кроссвордов!

    S    
    Y    
    N    
    T    
GRAPHICAL
    E    
    S    
    I    
    S    

Задача

Напишите функцию, которая принимает на вход две строки и выводит пересечение двух слов.
Вход

Две струны, str1 и str2.

    Длина каждого слова не более 20 символов.
    Слова могут быть разной длины.
    Слова будут написаны заглавными буквами и не будут содержать других символов.
    В словах всегда будет как минимум одна общая буква, поэтому вам не придется беспокоиться о недопустимых падежах.

Выход

    Ваша функция должна выводить первое слово по горизонтали, а второе слово — по вертикали.
    Слова пересекаются в точке первого появления общей буквы во втором слове .
    Для заполнения пробелов используется символ пробела.
    Каждая строка заканчивается символом новой строки.

Пример

str1 = "GRAPHICAL"
str2 = "SYNTHESIS"

возвращает образец сверху.

"""
import typing
import unittest


def crossedwords(str1: str, str2: str) -> str:
    """
    Составляет кроссворд.
    """
    a, b = next((i, str1.find(x)) for i, x in enumerate(str2) if x in str1)
    return ''.join([f'{" " * b + x:<{len(str1)}}', str1][i == a] + '\n' for i, x in enumerate(str2))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(crossedwords, (
        (('X', 'X'), (
            'X\n')
        ),

        (('ABXC', 'WXYZ'), (
            '  W \n'
            'ABXC\n'
            '  Y \n'
            '  Z \n')
        ),

        (('GRAPHICAL', 'SYNTHESIS'), (
            '    S    \n'
            '    Y    \n'
            '    N    \n'
            '    T    \n'
            'GRAPHICAL\n'
            '    E    \n'
            '    S    \n'
            '    I    \n'
            '    S    \n')
        ),

        (('A', 'BBBA'), (
            'B\n'
            'B\n'
            'B\n'
            'A\n')
        ),

        (('AAAB', 'B'), (
            'AAAB\n')
        ),

        (('ABCC', 'DCBA'), (
            '  D \n'
            'ABCC\n'
            '  B \n'
            '  A \n')
        ),
    ))
