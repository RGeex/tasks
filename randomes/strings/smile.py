"""
Мы часто используем смайлы в переписке с другими людьми. Они позволяют нам
быстро показать нашу реакцию на человека(ов), с которым мы разговариваем.

Но однажды вам захотелось сделать вашу переписку более радостной. Итак,
сегодня у вас есть возможность воплотить это в жизнь.
Задача:

В этом ката вашей задачей будет заменить грустные смайлы на веселые.

Смайлики будут представлены:

    Глаза: отмечены как :, ; или =
    Нос (необязательно): отмечен как - или ~
    Рот: отмечен как ( или [

Примеры:

smile("Howdy :(")  // should return "Howdy :)"
smile("Never be sad =[")  // should return "Never be sad =]"
smile("Change this `=(` and this `:[`")  // should return "Change this `=)`
and this `:]`"
"""


import re


def smile(text: str) -> str:
    """
    Заменяет грустные смайлы в тексте на веселые.
    """
    return re.sub(r'[:;=][-~]?[([]', lambda x: x[0].translate(str.maketrans('([', ')]')), text)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('Howdy :(', 'Howdy :)'),
        ('Never be sad =[', 'Never be sad =]'),
        ('It\'s been raining all day ;-(', 'It\'s been raining all day ;-)'),
        ('My friend got married ;~[', 'My friend got married ;~]'),
        ('Change this `=(` and this `:[`', 'Change this `=)` and this `:]`'),
        ('Funny smileys: ;~[ :( :-( :~[ :-[', 'Funny smileys: ;~] :) :-) :~] :-]'),
        ('The list of positive numbers is [1,2,3,4...]', 'The list of positive numbers is [1,2,3,4...]'),
        ('(((-)(((-)))(-)))', '(((-)(((-)))(-)))'),
    )
    for key, val in data:
        assert smile(key) == val


if __name__ == '__main__':
    test()
