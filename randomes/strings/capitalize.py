"""
Дана строка, сделайте заглавными буквы, которые занимают четные и нечетные индексы по отдельности,
и верните результат, как показано ниже. Индекс 0будет считаться четным.

Например, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. Дополнительные примеры см. в тестовых
случаях.

Входные данные будут представлять собой строку в нижнем регистре без пробелов.
"""
import typing
import unittest


def capitalize(st: str) -> list[str]:
    """
    Из строки создает список CamelCase для каждой буквы.
    """
    return list(map(''.join, zip(*[[x, x.upper()][::i % 2 or -1] for i, x in enumerate(st.lower())]))) or ['', '']


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(capitalize, (
        ("abcdef", ['AbCdEf', 'aBcDeF']),
        ("codewars", ['CoDeWaRs', 'cOdEwArS']),
        ("abracadabra", ['AbRaCaDaBrA', 'aBrAcAdAbRa']),
        ("codewarriors", ['CoDeWaRrIoRs', 'cOdEwArRiOrS']),
        ("indexinglessons", ['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs']),
        ("codingisafunactivity", ['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY']),
    ))
