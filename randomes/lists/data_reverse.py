"""
Поток данных получен, и его необходимо реверсировать.

Каждый сегмент имеет длину 8 бит, что означает, что порядок этих сегментов
необходимо изменить на обратный, например:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

должно стать:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)

Общее количество бит всегда будет кратно 8.

Данные задаются в виде массива:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
"""


def data_reverse(data: list) -> list:
    """
    Переворачиват полученные байты переданных данных.
    """
    return [n for x in [data[i*8:i*8+8] for i in range(len(data) // 8)][::-1] for n in x]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
        ),
        (
            [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1],
            [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0],
        ),
    )
    for key, val in data:
        assert data_reverse(key) == val


if __name__ == '__main__':
    test()
