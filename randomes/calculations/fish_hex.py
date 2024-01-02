"""
Сколько рыбы! (- Самокат )

Океан полон разноцветных рыб. Мы, программисты, хотим знать шестнадцатеричное значение этих рыб.
Задача

Возьмите все шестнадцатеричные допустимые символы (a,b,c,d,e,f) данного имени и выполните XOR их.
Верните результат как целое число.
Вход

Входные данные всегда представляют собой строку, которая может содержать пробелы, буквы верхнего и
нижнего регистра, но не содержать цифр.
Пример

fisHex("redlionfish") -> e,d,f -> XOR -> 12

"""
from functools import reduce


def fish_hex(s: str) -> int:
    """
    XOR 16-тиричных буквенных значений в заданной строке.
    """
    return reduce(lambda a, b: a ^ b, [int(x, 16) for x in s.lower() if x in 'abcdef'] or [0])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('', 0),
        ("pufferfish", 1),
        ("puffers", 14),
        ("balloonfish", 14),
        ("blowfish", 4),
        ("bubblefish", 10),
        ("globefish", 10),
        ("swellfish", 1),
        ("toadfish", 8),
        ("toadies", 9),
        ("honey toads", 9),
        ("sugar toads", 13),
        ("sea squab", 5),
    )
    for key, val in data:
        assert fish_hex(key) == val


if __name__ == '__main__':
    test()
