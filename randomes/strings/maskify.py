"""
Обычно, когда вы что-то покупаете, вас спрашивают, верны ли номер вашей кредитной карты,
номер телефона или ответ на самый секретный вопрос. Однако, поскольку кто-то может
заглянуть вам через плечо, вы не хотите, чтобы это было показано на экране.
Вместо этого мы это маскируем.

Ваша задача — написать функцию maskify, который изменяет все символы,
кроме последних четырех, на '#'.
Примеры (вход -> выход):

"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"


"""
import typing
import unittest


def maskify(st: str) -> str:
    """
    Скрывает все символы строки, кроме последних 4-х.
    """
    return '#' * (len(st) - 4) + st[-4:]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(maskify, (
        ('', ''),
        ('123', '123'),
        ('SF$SDfgsd2eA', '########d2eA'),
    ))
