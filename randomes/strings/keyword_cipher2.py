"""
Шифр с ключевым словом — это одноалфавитный шифр, в котором для шифрования
используется «ключевое слово». Это чем-то похоже на шифр Цезаря.

В шифре с ключевым словом повторы букв в ключевом слове удаляются, а алфавит
переупорядочивается таким образом, что буквы в ключевом слове появляются первыми,
а затем остальные буквы алфавита в их обычном порядке.

Например, для латинского алфавита в верхнем регистре с ключевым словом «KEYWORD»:

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

становится:

K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

такой, что:

cipher.encode('ABCHIJ') == 'KEYABC'
cipher.decode('KEYABC') == 'ABCHIJ'

Все буквы в ключевом слове также будут в алфавите. Для целей этой ката следует
использовать только первое появление буквы в ключевом слове. Любые символы, не
предусмотренные в алфавите, следует оставлять на месте при кодировании или
декодировании.
"""


class keyword_cipher(object):
    """
    Кодировка и декодировка строки по ключевому слову.
    """
    def __init__(self, abc: str, keyword: str) -> None:
        key = ''.join(sorted(set(keyword), key=keyword.index) + [x for x in abc if x not in keyword])
        self.a = str.maketrans(abc, key)
        self.b = str.maketrans(key, abc)

    def encode(self, plain: str) -> str:
        """
        Кодировка строки.
        """
        return plain.translate(self.a)
    
    def decode(self, ciphered: str) -> str:
        """
        Декодировка строки.
        """
        return ciphered.translate(self.b)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "keyword"
    cipher = keyword_cipher(abc, key)

    data = (
        (cipher.encode("abc"), "key"),
        (cipher.encode("xyz"), "vxz"),
        (cipher.decode("key"), "abc"),
        (cipher.decode("vxz"), "xyz"),
    )
    for key, val in data:
        assert key == val


if __name__ == '__main__':
    test()
