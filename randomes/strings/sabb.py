"""
Обучение программированию в рамках основной работы поглощает всю вашу жизнь.
Вы понимаете, что для быстрого достижения значительных успехов было бы полезно
пройти курс программирования в Лондоне.

Проблема в том, что многие из них стоят целое состояние, а те, которые не
требуют больших временных затрат, все равно подразумевают значительное
количество свободного времени — кто будет выплачивать вашу ипотеку?!

Чтобы компенсировать этот риск, вы решаете, что вместо того, чтобы полностью
уйти с работы, вы запросите отпуск, чтобы иметь возможность вернуться на работу
после учебного лагеря и получать заработную плату, пока вы ищете новую работу.

Вам нужно обратиться к своему руководителю. Её решение будет основано на трёх
факторах:

val= ваша ценность для организации
happiness= ее уровень счастья на момент вопроса и, наконец,
Количество букв слова «sabbatical», присутствующих в строке s.

Обратите внимание, что если s содержит три экземпляра буквы «л», что все равно
дает три балла, хотя в слове sabbatical она встречается только одна.

Если сумма трех параметров (как описано выше) > 22, вернуть «Отпуск! Бум!», в
противном случае вернуть «Вернись за свой стол, парень».
"""
import typing
import unittest
import re


def sabb(s: str, val: int, happiness: int) -> str:
    """
    Определяет, дадут ли отпуск.
    """
    return ["Back to your desk, boy.", "Sabbatical! Boom!"][sum([len(re.findall(r'(?i)[sabbatical]', s)), val, happiness]) > 22]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sabb, (
        (("Can I have a sabbatical?", 5, 5), "Sabbatical! Boom!"),
        (("Why are you shouting?", 7, 2), "Back to your desk, boy."),
        (("What do you mean I cant learn to code??", 8, 9), "Sabbatical! Boom!"),
        (("Please calm down", 9, 1), "Back to your desk, boy."),
    ))
