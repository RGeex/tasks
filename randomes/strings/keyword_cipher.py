"""
Третий день на вашей новой работе криптоаналитика, и вы сталкиваетесь с самым
сложным заданием. Ваша задача — реализовать простой шифр с ключевым словом.
Шифр с ключевым словом — это тип одноалфавитной подстановки, при которой два
параметра предоставляются как таковые (строка, ключевое слово). Строка
шифруется путем взятия ключевого слова и удаления всех букв, которые
встречаются более одного раза. Остальные буквы алфавита, которые не
используются, добавляются в конец ключевого слова.

Например, если ваша строка была «привет», а ключевое слово — «среда», ваш ключ
шифрования будет «wednsaybcfghijklmopqrtuvxz».

Чтобы зашифровать «привет», вы должны заменить это следующим образом:

              abcdefghijklmnopqrstuvwxyz
  hello ==>   |||||||||||||||||||||||||| ==> bshhk
              wednsaybcfghijklmopqrtuvxz

hello зашифровывается в bshhk с ключевым словом среда. В этом шифре также
используются только строчные буквы.

Удачи.
"""


from string import ascii_lowercase as abc


def keyword_cipher(msg: str, keyword: str) -> str:
    """
    Производит шифрование строки по заданному ключевому слову.
    """
    return msg.lower().translate(str.maketrans(abc, ''.join(sorted((x := set(keyword)), key=keyword.index) + sorted(set(abc) - x))))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("Welcome home","secret"), "wticljt dljt"),
        (("hello","wednesday"), "bshhk"),
        (("HELLO","wednesday"), "bshhk"),
        (("HeLlO","wednesday"), "bshhk"),
        (("WELCOME HOME", "gridlocked"), "wlfimhl kmhl"),
        (("alpha bravo charlie", "delta"), "djofd eqdvn lfdqjga"),
        (("Home Base", "seven"), "dlja esqa"),
        (("basecamp", "covert"), "ocprvcil"),
        (("one two three", "rails"), "mks twm tdpss"),
        (("Test", "unbuntu"), "raqr"),
    )
    for key, val in data:
        assert keyword_cipher(*key) == val


if __name__ == '__main__':
    test()
