"""
Введение

Шифр ragbaby — это шифр замены, который кодирует/декодирует текст с
использованием алфавита с ключами и их позиции в слове открытого
текста, частью которого они являются.

Чтобы зашифровать текст This is an example. с ключом cipher, сначала
создайте ключевой алфавит:

cipherabdfgjklmnoqstuvwxyz

Затем пронумеруйте буквы в тексте следующим образом:

This is an example.
1234 12 12 1234567.

Чтобы получить закодированный текст, замените каждый символ слова буквой
кодового алфавита на соответствующее количество мест справа от нее
(перенос при необходимости). Неалфавитные символы сохраняются для
обозначения границ слов.

Тогда наш зашифрованный текст Urew pu bq rzfsbtj.
Задача

Функции Wirate encode и decode которые принимают 2 параметра:

    text - строка - текст для кодирования/декодирования
    key - строка - ключ

Примечания

    обрабатывать нижний и верхний регистр в text нить
    key состоит только из символов нижнего регистра
"""


def encode(text: str, key: str, code: int=1) -> str:
    """
    Кодирует строку шифром ragbaby.
    """
    cip, res, num = sorted(set(key), key=key.index) + [w for i in range(26) if (w := chr(i + 97)) not in key], '', 1
    for x in text:
        res, num = (res + [c := cip[(cip.index(x.lower()) + [-num, num][code]) % 26], c.upper()][x.isupper()], num + 1) if x.isalpha() else (res + x, 1)
    return res


def decode(text: str, key: str) -> str:
    """
    Декодирует строку шифром ragbaby.
    """
    return encode(text, key, 0)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("cipher", "cipher"), "ihrbfj" ),
        (("cipher", "cccciiiiippphheeeeerrrrr"), "ihrbfj"),
        (("This is an example.", "cipher"), "Urew pu bq rzfsbtj." ),
        (("This.tHis.thIs.thiS...", "cipher"), "Urew.uRew.urEw.ureW..." ),
    )
    for key, val in data:
        assert encode(*key) == val

    data = (
        (("ihrbfj", "cipher"), "cipher" ),
        (("Urew pu bq rzfsbtj.", "cipher"), "This is an example."),
        (("Urew.uRew.urEw.ureW...", "cipher"), "This.tHis.thIs.thiS..."),
    )
    for key, val in data:
        assert decode(*key) == val


if __name__ == '__main__':
    test()
