"""
Мэри принесла домой книгу «найди отличия». Книга полна задач, и каждая задача состоит из двух строк,
которые похожи. Однако в каждой строке есть несколько символов, которые отличаются.
Пример головоломки из ее книги:

String 1: "abcdefg"
String 2: "abcqetg"

Обратите внимание, как «d» из строки 1 превратилась в «q» в строке 2, а «f» из строки 1
превратилась в «t» в строке 2.

Ваша задача — помочь Мэри решить головоломки. Напишите программу spot_diff/ Spotкоторый
сравнит две строки и вернет список позиций, где две строки различаются. В примере выше
ваша программа должна вернуть [3, 5]поскольку строка 1 отличается от строки 2 в позициях 3 и 5.

ПРИМЕЧАНИЯ:

• Если обе строки одинаковы, вернуть []

• Обе строки всегда будут одинаковой длины.

• Заглавные буквы и знаки препинания имеют значение.
"""
import typing
import unittest


def spot_diff(s1: str, s2: str) -> list[int]:
    """
    Поиск индексов отличающихся символов между 2-х строк.
    """
    return [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(spot_diff, (
        (('abcdefg', 'abcqetg'), [3, 5]),
        (('Hello World!', 'hello world.'), [0, 6, 11]),
        (('FixedGrey', 'FixedGrey'), []),
    ))
