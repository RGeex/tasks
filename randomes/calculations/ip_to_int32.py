"""
Возьмите следующий IPv4-адрес: 128.32.10.1. Этот адрес состоит из 4 октетов, каждый из которых
представляет собой один байт (или 8 бит).

    1-й октет 128 имеет двоичное представление: 10000000.
    2-й октет 32 имеет двоичное представление: 00100000.
    3-й октет 10 имеет двоичное представление: 00001010.
    4-й октет 1 имеет двоичное представление: 00000001.

Так 128.32.10.1 == 10000000.00100000.00001010.00000001

Поскольку приведенный выше IP-адрес имеет 32 бита, мы можем представить его как 32-битный.
номер бита: 2149583361.

Напишите функцию ip_to_int32(ip)( ДжС : ipToInt32(ip)), который принимает адрес IPv4 и
возвращает 32-битное число.
Пример

"128.32.10.1" => 2149583361
"""


def ip_to_int32(ip: str) -> int:
    """
    Конвертирует IP адресс из строки в 32-битное число.
    """
    return sum(int(x) << i * 8 for i, x in enumerate(ip.split('.')[::-1]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("128.114.17.104", 2154959208),
        ("0.0.0.0", 0),
        ("128.32.10.1", 2149583361),
    )
    for key, val in data:
        assert ip_to_int32(key) == val


if __name__ == '__main__':
    test()