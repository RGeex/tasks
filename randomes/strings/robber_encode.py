"""
Введение

«Язык разбойников» (Rövarspråket) — шведский жаргон, используемый детьми для того,
чтобы вводить в заблуждение людей, не знакомых с этим языком. Он используется
детьми в нескольких сценариях Астрид Линдгрен .

Идея состоит в том, что каждая согласная в предложении дублируется , с o
вставлен между ( bстановится bob). Гласные остаются нетронутыми ( aостается a).
Неподготовленному уху довольно сложно понять закодированную таким образом речь,
особенно если она произносится быстро.
Пример

В этом примере согласные f, b и rИзменены. Гласные o и aостаются нетронутыми.

'foo bar' => 'fofoo bobaror' (`fof-o-o bob-a-ror`)

Примечание : тире -в примере добавлены для удобства чтения и не должны
включаться в вывод.
Задание

Ваша задача — реализовать функцию def robber_encode(sentence)который
принимает строку sentenceи возвращает результат, преобразованный в язык
разбойника , в виде строки.
Примечания

    только согласные ; все остальные символы оставить без изменений.
    Изменять следует
    как заглавные , так и строчные символы. Будут проверяться
    Случай с ​ oсимвол и соседние согласные должны совпадать ( F => FOF и f => fof).
    В рамках этого ката символ считается согласным, если он равен одной из
    букв BCDFGHJKLMNPQRSTVWXYZ.

Тестирование

Тесты проверят вашу функцию на основе предложений длиной от 0 до 255 символов,
символов ASCII от 32 до 126 и ничего больше .
Ссылки

Для получения более подробной информации перейдите по этим ссылкам:

    https://en.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket
"""
import typing
import unittest
import re


def robber_encode(sentence: str) -> str:
    """
    Переводит строку на язык разбойников.
    """
    return re.sub(r'(?i)([BCDFGHJKLMNPQRSTVWXYZ])', lambda m: f'{(x := m.group())}{["o", "O"][x.isupper()]}{x}', sentence)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(robber_encode, (
        ("hello world", "hohelollolo wowororloldod"),
        ("coding is fun", "cocododinongog isos fofunon"),
        ("follow the white rabbit", "fofolollolowow tothohe wowhohitote rorabobbobitot"),
        ("S.O.S", "SOS.O.SOS"),
    ))
