"""
Боб — программист-теоретик: он не пишет код, а придумывает теории, формулы и
идеи для алгоритмов. Вы — его секретарь, и он поручил вам написать код для
своего нового проекта — метода создания сокращённой формы слова.
Напишите функцию. shortForm(С#) ShortForm, Питон short_form),
которая принимает строку и возвращает её, преобразованную в
сокращённую форму, по правилу: удалить все гласные, кроме тех,
которые являются первой или последней буквой. Не считать «y»
гласной и игнорировать регистр. Также обратите внимание,
что в указанной строке не будет пробелов; только одно слово,
состоящее только из латинских букв.
Пример:

shortForm("assault");
short_form("assault")
ShortForm("assault");
// should return "asslt"

"""
import typing
import unittest


def short_form(st: str) -> str:
    """
    Удаляет все гласные буквы из слова кроме первой и последней игнорируя регистр.
    """
    return ''.join([[x, ''][x.lower() in 'aeiou'], x][i in (0, len(st) - 1)] for i, x in enumerate(st))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(short_form, (
        ("typhoid", "typhd"),
        ("fire", "fre"),
        ("destroy", "dstry"),
        ("kata", "kta"),
        ("codewars", "cdwrs"),
        ("assert", "assrt"),
        ("insane", "insne"),
        ("nice", "nce"),
        ("amazing", "amzng"),
        ("incorrigible", "incrrgble"),
        ("HeEllO", "HllO"),
        ("inCRediBLE", "inCRdBLE"),
        ("IMpOsSiblE", "IMpsSblE"),
        ("UnInTENtiONAl", "UnnTNtNl"),
        ("AWESOme", "AWSme"),
        ("rhythm", "rhythm"),
        ("hymn", "hymn"),
        ("lynx", "lynx"),
        ("nymph", "nymph"),
        ("pygmy", "pygmy"),
    ))
