"""
Вам дана строка слов (х), для каждого слова в строке нужно вывернуть слово
«наизнанку». Под этим я подразумеваю, что внутренние буквы будут двигаться
наружу, а внешние — к центру.

Если слово четной длины, все буквы будут двигаться. Если длина нечетная,
ожидается, что вы оставите «среднюю» букву слова там, где она есть.

Пример должен прояснить:

'taxi' would become 'atix' 'taxis' would become 'atxsi'
"""


import re


def inside_out(s: str) -> str:
    """
    Разделяет строку на слова (сохраняя кол-во пробелов) и выворачивает каждое слово.
    """
    return ''.join([w[:len(w)//2][::-1]+['', w[len(w)//2]][len(w)%2]+w[len(w)//2+len(w)%2:][::-1] for w in re.split(r'\b', s) if w])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('take me to semynak', 'atek me to mesykan'),
        ('man i need a taxi up to ubud', 'man i ende a atix up to budu'),
        ('what time are we climbing up the volcano', 'hwta item are we milcgnib up the lovcona'),
    )
    for key, val in data:
        assert inside_out(key) == val


if __name__ == '__main__':
    test()
