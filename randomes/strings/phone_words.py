"""
Учитывая строку чисел, вы должны выполнить метод, с помощью которого вы
преобразуете эту строку в текст, на основе изображения ниже:

Например, если вы получаете "22" возвращаться "b", если ты получишь "222"
ты вернешься "c". Если вы получите "2222" возвращаться "ca".

Дополнительная информация:

    0 это пробел в строке.
    1 используется для разделения букв с одинаковым номером.
    всегда преобразуйте число в букву с максимальным значением, если у нее нет
    1 в середине. Так, "777777" -->  "sq" и "7717777" --> "qs".
    вы не можете возвращать цифры.
    Учитывая пустую строку, верните пустую строку.
    Вернуть строку в нижнем регистре.

Примеры:

"443355555566604466690277733099966688"  -->  "hello how are you"
"55282"                 -->  "kata"
"22266631339277717777"  -->  "codewars"
"66885551555"           -->  "null"
"833998"                -->  "text"
"000"                   -->  "   "
"""


from itertools import groupby as gb


def phone_words(num: str) -> str:
    """
    Преобразует набор на кнопочном телефоне цифр в буквы алфавита.
    """
    word = ' ..abc.def.ghi.jkl.mno.pqrs.tuv.wxyz'.split('.')
    return ''.join(''.join(w[[0, n][i] - 1] * (i or n) for i, n in enumerate(divmod(*map(len, (list(b), w)))) if n) for a, b in gb(num) if (w := word[int(a)]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("443355555566604466690277733099966688","hello how are you"),
        ("55282", "kata"),
        ("44460208337777833777", "im a tester"),
        ("22266631339277717777", "codewars"),
        ("66885551555", "null"),
        ("833998", "text"),
        ("000", "   "),
        ("7999844666166", "python"),
        ("55886444833", "kumite"),
        ("271755533", "apple"),
        ("", ""),
        ("111", ""),
    )
    for key, val in data:
        assert phone_words(key) == val


if __name__ == '__main__':
    test()