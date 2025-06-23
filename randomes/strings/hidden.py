"""
Майя пишет еженедельные статьи в известный журнал, но каждый раз, когда она собирается отправить
статью редактору, ей не хватает одного слова. Статья не будет полной без этого слова. У Майи есть
друг Дэн, и он очень хорошо владеет словами, но он не любит просто так их раздавать. Он отправляет
Майе сообщение с номером, и ей нужно узнать спрятанное слово. Слова могут содержать только букву:

"a", "b", "d", "e", "i", "l", "m", "n", "o", and "t".

К счастью, у Майи есть ключ:

"a" : 6
"b" : 1 
"d" : 7
"e" : 4
"i" : 3
"l" : 2
"m" : 9
"n" : 8
"o" : 0
"t" : 5

Вы можете помочь Maya, написав функцию, которая будет принимать число от 100 до 999999 и возвращать
строку со словом.

Входные данные всегда являются числом и содержат только цифры ключа. Вывод всегда должен представлять
собой строку из одного слова, все буквы строчные.

Майя не забудет поблагодарить вас в конце своей статьи :)

"""
import typing
import unittest


def hidden(num: int) -> str:
    """
    Заменяет цифры буквами по заданному шаблону.
    """
    return str(num).translate(str.maketrans('0123456789', 'oblietadnm'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(hidden, (
        (637, "aid"),
        (7415, "debt"),
        (49632, "email"),
        (942547, "melted"),
    ))
