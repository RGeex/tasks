"""
Шаг 1. Создайте функцию с именем encode()заменить все строчные гласные в
данной строке числами по следующему шаблону:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

Например, encode("hello")вернусь "h2ll4". В этой ката не нужно беспокоиться о
гласных в верхнем регистре.

Шаг 2: Теперь создайте функцию под названием decode()чтобы превратить числа
обратно в гласные согласно той же схеме, что показана выше.

Например, decode("h3 th2r2")вернусь "hi there".

Для простоты можно предположить, что любые числа, переданные в функцию, будут
соответствовать гласным.
"""


enc, dec = [dict(map(str, x[::i or -1]) for x in enumerate('aeiou', 1)) for i in range(2)]


def encode(st: str) -> str:
    """
    Кодирование строки.
    """
    return ''.join([enc.get(x, x) for x in st])


def decode(st: str) -> str:
    """
    Декодирование строки.
    """
    return ''.join([dec.get(x, x) for x in st])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = ( 
        ('hello', 'h2ll4'),
        ('How are you today?', 'H4w 1r2 y45 t4d1y?'),
        ('This is an encoding test.', 'Th3s 3s 1n 2nc4d3ng t2st.'),
    )
    for key, val in data:
        assert encode(key) == val
    assert decode('h2ll4') == 'hello'


if __name__ == '__main__':
    test()
