"""
На Бали, насколько я могу судить, когда экспаты говорят с местными, они в основном вставляют слово
«Pak» как можно чаще. Я уверен, что это означает что-то вроде «приятель» или «сэр», но это может
быть совершенно неверно.

В любом случае, в качестве некоторого базового языкового образования(??) эта ката требует от вас
превратить любое предоставленное предложение(я) в вафлю на балийском языке, вставив слово «pak»
между каждым другим словом.

Pak не должно быть первым или последним словом. Строки, состоящие только из пробелов, должны
возвращать пустую строку.
"""
import typing
import unittest


def pak(st: str) -> str:
    """
    Вставляет слово "pak", между другими словами.
    """
    return ' pak '.join(st.split())



def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(pak, (
        ("Man I need a taxi up to Ubud", "Man pak I pak need pak a pak taxi pak up pak to pak Ubud"),
        ("What time are we climbing up the volcano?", "What pak time pak are pak we pak climbing pak up pak the pak volcano?"),
        ("Take me to Semynak!", "Take pak me pak to pak Semynak!"),
        ("Massage Yes Massage Yes Massage!", "Massage pak Yes pak Massage pak Yes pak Massage!"),
        ("I'll take 12 bintang and a dance please", "I'll pak take pak 12 pak bintang pak and pak a pak dance pak please"),

    ))
