"""
Исправлено xor

Напишите функцию, которая принимает на вход две шестнадцатеричные строки и выполняет их операцию
XOR друг против друга. Если строки имеют разную длину, на выходе должна быть длина самой короткой
строки.

Подсказка: для выполнения операции XOR строки сначала необходимо преобразовать в двоичный формат.
Примечание:

Если две строки имеют разную длину, выходная строка должна иметь ту же длину, что и наименьшая
строка. Это означает, что более длинная строка будет обрезана до того же размера, что и меньшая
строка, а затем будет выполнено xor.
"""


def fixed_xor(a: str, b: str) -> str:
    """
    XOR 2-х 16-тиричных чисел по минимальной длине.
    """
    return ''.join(f'{int(x, 16) ^ int(y, 16):x}' for x, y in zip(a, b))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"),
         "746865206b696420646f6e277420706c6179"),
        (("aadf", "bce2"), "163d"),
        (("ab3f", "ac"), "07"),
        (("", ""), ""),
        (("c611d9bdd9de38b9eb", "23a0745505d4d25494"), "e5b1ade8dc0aeaed7f"),
        (("7d1e875da9d5e89b54c7eaf", "3541599be591709795cebd5"), "485fdec64c44980cc10957a"),
        (("785a6677b3e52f0e7", "a8d97da7441"), "d0831bd0f7f"),
        (("6cbd75511e7f750c6827", "1753547c813bfcd"), "7bee212d9f4489d"),
    )
    for key, val in data:
        assert fixed_xor(*key) == val


if __name__ == '__main__':
    test()