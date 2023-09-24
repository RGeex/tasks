"""
Ваша задача — создать функцию-шифровальщик, которая принимает 2 аргумента:
ключ и сообщение и возвращает зашифрованное сообщение.

Удостоверьтесь, что вы меняете только буквы и следите за тем, чтобы регистры
букв оставались одинаковыми. Все знаки препинания, цифры, пробелы и т.д.
должны оставаться прежними.

Также помните о ключах больше 26 и меньше -26. В алфавите всего 26 букв! 
"""


def encryptor(key: int, message: str) -> str:
    """
    Алгоритм шифра Цезаря.
    """
    result = ''
    for char in message:
        if char.isalpha():
            mode = [97, 65][char.isupper()]
            char = chr((ord(char) + key - mode) % 26 + mode)
        result += char
    return result


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((13, ''), ''),
        ((-5, 'Hello World!'), 'Czggj Rjmgy!'),
        ((13, 'Caesar Cipher'), 'Pnrfne Pvcure'),
        ((27, 'Whoopi Goldberg'), 'Xippqj Hpmecfsh'),
    )

    for key, val in data:
        assert encryptor(*key) == val


if __name__ == '__main__':
    test()
