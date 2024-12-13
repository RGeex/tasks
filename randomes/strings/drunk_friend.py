"""
Вы тусуетесь с друзьями в баре, как вдруг один из них настолько пьян, что не
может говорить, и когда он хочет что-то сказать, он записывает это на бумаге.
Однако ни одно из слов, которые он пишет, не имеет для вас смысла. Он хочет
вам помочь, поэтому указывает на пиво и пишет «ывви». Вы начинаете понимать,
что он пытается сказать, и пишете сценарий, который расшифровывает его слова.

Имейте в виду, что числа, как и другие символы, могут быть частью входных
данных, и вам следует оставить их такими, какие они есть. Вам также следует
проверить, является ли ввод строкой. Если это не так, верните «Ввод не
является строкой».
"""


from string import ascii_letters as abc


def drunk_friend(s: str) -> str:
    """
    Декодирует речь пьяного друга в воспринимаемый язык.
    """
    return s.translate((str.maketrans(abc, abc[25::-1] + abc[:25:-1]))) if isinstance(s, str) else "Input is not a string"


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("yvvi", "beer"),
        ("Blf zoivzwb szw 10 yvvih", "You already had 10 beers"),
        ("Ovg'h hdrn rm gsv ulfmgzrm!", "Let's swim in the fountain!"),
        ({"brand": "Starobrno" }, "Input is not a string"),
        ("Tl slnv, blf'iv wifmp", "Go home, you're drunk") ,
        ("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi", "Sure i can dance on cop's car, hold my beer"),
        (True, "Input is not a string"),
        ("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu", "See? I'm not that drunk, i can still take my clothes off"),
        (123, "Input is not a string"),
        (["Beer"], "Input is not a string"),
        ('byN1CGTZgWARi3ABU.5IhzpLiM', 'ybM1XTGAtDZIr3ZYF.5RsakOrN'),
        ('x!t0C1j9YYi1m6STg6yv', 'c!g0X1q9BBr1n6HGt6be'),
        ('L7 A9;KleF. :HHJR39;eZypFem6JX', 'O7 Z9;PovU. :SSQI39;vAbkUvn6QC'),
        ('K?nE.qvnoEy BB', 'P?mV.jemlVb YY'),
    )
    for key, val in data:
        assert drunk_friend(key) == val


if __name__ == '__main__':
    test()
