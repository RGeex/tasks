"""
Кейт любит считать слова в текстовых блоках. Под словами она подразумевает
непрерывные последовательности символов английского алфавита (от a до z).
Вот примеры:

Hello there, little user5453 374 ())$. I’d been using my sphere as a stool.
Slow-moving target 839342 was hit by OMGd-63 or K4mp. содержит «слова»
['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere',
'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd',
'or', 'K', 'mp']

Кейт не любит некоторые слова и не считает их. Исключаются слова «a», «the»,
«on», «at», «of», «on», «in» и «as», без учета регистра.

Сегодня Кейт слишком ленива и решила научить свой компьютер считать за нее
«слова».
"""


import re


def word_count(s: str) -> int:
    """
    Считает кол-во допустимых слов в предложении.
    """
    return len(list(filter(lambda x: x not in 'a the on at of on in as'.split(), re.sub(r'[^a-zæ ]', ' ', s.lower()).split())))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("hello there", 2),
        ("hello there and a hi", 4),
        ("I'd like to say goodbye", 6),
        ("Slow-moving user6463 has been here", 6),
        ("%^&abc!@# wer45tre", 3),
        ("abc123abc123abc", 3),
        ("Really2374239847 long ^&#$&(*@# sequence", 3),
    )
    for key, val in data:
        assert word_count(key) == val


if __name__ == '__main__':
    test()
