"""
Многие люди предпочитают скрывать свой адрес электронной почты, когда показывают его в Интернете.
Один из распространенных способов сделать это — заменить @ и .символы для их буквальных
эквивалентов в скобках.

Пример 1:

user_name@example.com
=> user_name [at] example [dot] com

Пример 2:

af5134@borchmore.edu
=> af5134 [at] borchmore [dot] edu

Пример 3:

jim.kuback@ennerman-hatano.com
=> jim [dot] kuback [at] ennerman-hatano [dot] com

Используя приведенные выше примеры в качестве руководства, напишите функцию, которая принимает
строку адреса электронной почты и возвращает запутанную версию в виде строки, которая заменяет
символы @ и . с [at] и [dot], соответственно.

    Примечания

        Вход ( email) всегда будет строковым объектом. Ваша функция должна возвращать строку.

        Измените только @ и .персонажи.

        Адреса электронной почты могут содержать более одного . характер.

        Обратите внимание на дополнительные пробелы вокруг литералов в квадратных скобках в
        примерах!
"""
import typing
import unittest


def obfuscate(email: str) -> str:
    """
    Скрывает адрес электронной почты заменяя собачку и дот.
    """
    return email.replace('.', ' [dot] ').replace('@', ' [at] ')



def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(obfuscate, (
        ('test@123.com', 'test [at] 123 [dot] com'),
        ('Code_warrior@foo.ac.uk', 'Code_warrior [at] foo [dot] ac [dot] uk'),
        ('user_name@example.com', 'user_name [at] example [dot] com'),
        ('af5134@borchmore.edu', 'af5134 [at] borchmore [dot] edu'),
        ('jim.kuback@ennerman-hatano.com', 'jim [dot] kuback [at] ennerman-hatano [dot] com'),
        ('sir_k3v1n_wulf@blingblong.net', 'sir_k3v1n_wulf [at] blingblong [dot] net'),
        ('Hmm, this would be better with input validation...!', 'Hmm, this would be better with input validation [dot]  [dot]  [dot] !'),
    ))
