"""
Панграмма – это предложение, которое содержит каждую букву алфавита хотя бы один раз.
Например, предложение «The quick brown fox jumps over the lazy dog» является панграммой,
поскольку в нем хотя бы один раз используются буквы AZ (регистр не имеет значения).

Учитывая строку, определите, является ли она панграммой. Возвращайте True, если это так, и False,
если нет. Не обращайте внимания на цифры и знаки препинания.
"""

import re


def is_pangram(s: str) -> bool:
    """
    Проверяет, является ли строка панаграммой.
    """
    return len(set(re.findall(r'[a-z]', s.lower()))) == 26


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        "Cwm fjord bank glyphs vext quiz",
        "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ",
        "How quickly daft jumping zebras vex.",
        "Pack my box with five dozen liquor jugs.",
        "The quick brown fox jumps over the lazy dog.",
    )
    for key in data:
        assert is_pangram(key)

    data = (
        "This isn't a pangram!",
        "abcdefghijklm opqrstuvwxyz",
        "Aacdefghijklmnopqrstuvwxyz",
    )
    for key in data:
        assert not is_pangram(key)


if __name__ == '__main__':
    test()
