"""
Ваш друг Робби успешно создал ИИ, способный общаться на английском языке!

Робби почти закончил проект, но вывод машины не соответствует ожиданиям.
Вот пример предложения, которое она выводит:

["this","is","a","sentence"]

Каждый раз, когда он пытается произнести предложение, вместо того, чтобы
отформатировать его в соответствии с обычной английской орфографией,
он просто выводит список слов.

Робби не спал ночами, чтобы закончить этот проект, и ему нужен хороший сон.
Поэтому он хочет, чтобы вы написали последнюю часть его кода, sentencifyфункция,
которая берет выходные данные, выдаваемые машиной, и форматирует их в
соответствии с правильной английской орфографией.

Ваша функция должна:

    Напишите заглавную первую букву первого слова.
    Добавьте точку ( .) в конец предложения.
    Объедините слова в единую строку, разделяя пробелами.
    Не делайте никаких других манипуляций со словами.

Вот несколько примеров того, что должна делать ваша функция:
Вход 	Выход
["i", "am", "an", "AI"] 	"I am an AI."
["FIELDS","of","CORN","are","to","be","sown"] 	"FIELDS of CORN are to be sown."
["i'm","afraid","I","can't","let","you","do","that"] 	"I'm afraid I can't let you do that."
"""
import typing
import unittest


def sentencify(words: list[str]) -> str:
    """
    Список слова объединяет в предложение, с заглавной первой буквой и точкой в конце.
    """
    return ' '.join([[w, w[0].upper() + w[1:]][not i] for i, w in enumerate(words)]) + '.'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sentencify, (
        (["i", "am", "an", "AI"], "I am an AI."),
        (["yes"], "Yes."),
        (["FIELDS","of","CORN","are","to","be","sown"], "FIELDS of CORN are to be sown."),
        (["i'm","afraid","I","can't","let","you","do","that"], "I'm afraid I can't let you do that."),
    ))
