"""
Вход:

    строка strng
    массив строк arr

Вывод функции contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

    булево значение trueесли все вращения strngвключены в arr
    false в противном случае

Примеры:

contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)

Примечание:

Хотя это и не правильно в математическом смысле

    мы будем считать, что нет никаких вращений strng == ""
    и для любого массива arr: contain_all_rots("", arr) --> true

"""
import typing
import unittest


def contain_all_rots(st: str, arr: list[str]) -> bool:
    """
    Проверяет наличие всех вращений слова в списке.
    """
    res = {}
    for word in arr:
        for i, v in enumerate(word):
            res[v] = res.get(v, set()) | {i, }
    return not any(set(range(len(st))) - res.get(x, set()) for x in st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(contain_all_rots, (
        (("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True),
        (("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False),
        (("QJAhQmS", ["hQmSQJA", "QJAhQmS", "QmSQJAh", "yUgUXoQE", "AhQmSQJ", "mSQJAhQ", "SQJAhQm", "JAhQmSQ"]), True),
        (("Etsshp", ["nVOETcaxdvuk", "shpEts", "hpEtss", "Etsshp", "OuIiQ", "sXrDdPXIaW", "tsshpE", "pEtssh"]), False),
        (("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl"]), False),
        (("MqhWvHF", ["numMfygcH", "HFMqhWv", "qhWvHFM", "ZJKKxM", "hWvHFMq", "MqhWvHF", "hfZWYSqk", "BTcSoEdchPlL", "WvHFMqh", "vHFMqhW", "FMqhWvH"]), True),
        (("UDvG", ["vGUD", "UDvG", "GUDv", "DvGU"]), True),
        (("sObPfw", ["ObPfws", "Cofuhqrmmzq", "wFvfcqU", "sObPfw", "bPfwsO", "PfwsOb", "wsObPf", "fwsObP"]), True),
        (("KUckM", ["MKUck", "EDjfbQB", "GUPwzk", "SKZvilwnL", "UckMK", "KUckM", "kMKUc"]), False),
        (("FDIe", ["DIeF", "IeFD", "FDIe", "eFDI"]), True),
        (("12341234", ["DIeF", "IeFD", "12341234", "41234123", "34123412", "23412341"]), True),
    ))
