"""
Гордон Рамзи кричит. Он кричит и ругается. С ним, наверное, что-то не так.

В любом случае, вам будет дана строка из четырех слов. Ваша задача — перевести их на язык Гордона.

Правила:

Очевидно, слова должны быть написаны заглавными буквами. Каждое слово должно заканчиваться на «!!!!»,
Любая буква «a» или «A» должна стать «@», Любая другая гласная должна стать «*».
"""
import typing
import unittest


def gordon(st: str) -> str:
    """
    Переводит предложения на язык Гордона.
    """
    return ' '.join([f'{x}!!!!' for x in st.upper().translate(str.maketrans('AEIOU', '@****')).split()])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(gordon, (
        ('What feck damn cake', 'WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!'),
        ('are you stu pid', '@R*!!!! Y**!!!! ST*!!!! P*D!!!!') ,
        ('i am a chef', '*!!!! @M!!!! @!!!! CH*F!!!!'),
        ('dont you talk tome', 'D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!') ,
        ('how dare you feck', 'H*W!!!! D@R*!!!! Y**!!!! F*CK!!!!'),
    ))
