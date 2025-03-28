"""
Помните мем про Спанч Боба, который призван высмеивать людей, повторяя то, что они говорят,
в издевательской форме?

«Не используй этот странный мем с насмешкой над Спанчбобом» Я: НЕ используй этот странный
мем с насмешкой над Спанчбобом

Вам необходимо создать функцию, которая преобразует входные данные в этот формат, при этом
на выходе получится та же строка, за исключением шаблона из заглавных и строчных букв.

Пример:

input:  "stop Making spongebob Memes!"
output: "StOp mAkInG SpOnGeBoB MeMeS!"


"""
import typing
import unittest


def sponge_meme(st: str) -> str:
    """
    Переписывает предложение в издевательской форме.
    """
    return ''.join([x.upper(), x][i % 2] for i, x in enumerate(st.lower()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sponge_meme, (
        ("stop Making spongebob Memes!", "StOp mAkInG SpOnGeBoB MeMeS!"),
    ))
