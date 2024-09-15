"""
Напишите модуль Converter, который может принимать текст ASCII и
преобразовывать его в шестнадцатеричный формат. Класс также должен
уметь принимать шестнадцатеричные числа и преобразовывать их в текст
ASCII. Чтобы сделать преобразование четко определенным, каждый символ
ASCII представлен ровно двумя шестнадцатеричными цифрами, дополняемыми
слева 0 если необходимо. Преобразование из ascii в шестнадцатеричный
формат должно привести к созданию строк в нижнем регистре
(т. е. f6 вместо F6).
Пример

Converter.to_hex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
"""


class Converter():
    """
    Преобразование строки hex в ascii.
    Преобразование строки ascii в hex.
    """
    @staticmethod
    def to_ascii(s: str) -> str:
        """
        Converted hex to ascii
        """
        return ''.join(chr(int(s[i*2:i*2+2], 16)) for i in range(len(s) // 2))
    
    @staticmethod
    def to_hex(s: str) -> str:
        """
        Converted ascii to hex
        """
        return ''.join(f"{ord(x):0>2x}" for x in s)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    s = "Look mom, no hands"
    h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"

    data = (
        (Converter.to_hex(s), h),
        (Converter.to_ascii(h), s),
        (Converter.to_hex(Converter.to_ascii(h)), h),
        (Converter.to_ascii(Converter.to_hex(s)), s),
    )
    for key, val in data:
        assert key == val


if __name__ == '__main__':
    test()
