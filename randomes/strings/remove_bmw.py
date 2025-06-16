"""
Это произошло за десятилетия до Snapchat, за годы до Twitter и даже до Facebook.
В то время целевая реклама была немного сложной задачей. Однажды профессор маркетинга
в моем университете рассказал нам историю, которую я еще не подтвердил с помощью надежных
источников. Тем не менее, я уже пересказал эту историю десяткам своих студентов, так что извините,
BMW, если все это большая ложь.

Предположительно, BMW, пытаясь привлечь образованную молодежь, выпустила рекламные щиты с
изображением английского алфавита, в котором отсутствовали три буквы: B, M и W. Излишне говорить,
что многие были в замешательстве, некоторые из них доходили до дорожных аварий.

Ваша задача — написать функцию, которая принимает один параметр str, который ДОЛЖЕН быть строкой,
и удаляет все заглавные и строчные буквы B, M и W.
Если в качестве параметра были отправлены данные неверного типа, функция должна выдать ошибку со
следующим конкретным сообщением:

TypeError("This program only works for text.")
"""
import re
import typing
import unittest


def remove_bmw(st: str) -> str:
    """
    Удаляет из слова все буквы bmw не зависимо от регистра, выдает ошибку если передана не строка.
    """
    return re.sub(r'(?i)[bmw]', '', st) if isinstance(st, str) else 'This program only works for text.'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_bmw, (
        ("bmwvolvoBMW", "volvo"),
        ("blablahblah", "lalahlah"),
    ))
