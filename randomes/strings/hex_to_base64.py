"""
Преобразовать строку в шестнадцатеричной кодировке
( https://en.wikipedia.org/wiki/Hexadecimal ) в base64
( https://en.wikipedia.org/wiki/Base64 )

Пример:

Строка:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Должно производить:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""


import codecs


def hex_to_base64(hex: str) -> str:
    """
    Декодирует hex в base64.
    """
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode().strip('\n')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
        'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'),
    )
    for key, val in data:
        assert hex_to_base64(key) == val


if __name__ == '__main__':
    test()
