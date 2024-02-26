"""
Предположим, мы знаем процесс, с помощью которого строка sбыл закодирован в
строку r(см. объяснение ниже). Цель ката — расшифровать эту строку. r
чтобы вернуть исходную строку s.
Объяснение процесса кодирования:

    ввод: строка sсостоит из строчных букв от «a» до «z» и целого положительного числа. num
    мы знаем, что существует переписка между abcde...uvwxyzи 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...
    если cявляется персонажем sсоответствующий номер которого x, подать заявку на xфункция f: x-> f(x) = num * x % 26, затем найдите chсоответствующий характер f(x)
    Накопите все это chв строке r
    объединять numи rи вернуть результат

Например:

encode("mer", 6015)  -->  "6015ekx"

m --> 12,   12 * 6015 % 26 = 4,    4  --> e
e --> 4,     4 * 6015 % 26 = 10,   10 --> k
r --> 17,   17 * 6015 % 26 = 23,   23 --> x

So we get "ekx", hence the output is "6015ekx"

Задача

Строка sбыл закодирован в строку rвышеуказанным процессом. завершите функцию,
чтобы вернуться s всякий раз, когда это возможно.
"""


import re
from re import findall as f


def decode1(s: str) -> str:
    """
    Декодирует строку обратно алгоритму кодирования.
    """
    x = re.split(r'(?<=\d)(?=[a-z])', s)
    if len(x) == 2 and x[0].isdigit() and x[1].isalpha():
        n, s = int(x[0]), x[1]
        if len({x * n % 26 for x in range(26)}) == 26:
            return ''.join(chr(next(x for x in range(26) if x * n % 26 == ord(w) - 97) + 97) for w in s)
    return 'Impossible to decode'


def decode2(s: str) -> str:
    """
    Декодирует строку обратно алгоритму кодирования.
    """
    n, s = re.split(r'(?<=\d)(?=[a-z])', s)
    data = {chr(i * int(n) % 26 + 97): chr(i + 97) for i in range(26)}
    return ''.join(data.get(w) for w in s) if len(data) == 26 else 'Impossible to decode'


def decode3(s: str) -> str:
    """
    Декодирует строку обратно алгоритму кодирования.
    """
    data = {chr(i * int(f('\d+', s)[0]) % 26 + 97): chr(i + 97) for i in range(26)}
    return ''.join(data.get(w) for w in f('\D+', s)[0]) if len(data) == 26 else 'Impossible to decode'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx"),
        ("761328qockcouoqmoayqwmkkic", "Impossible to decode"),
        ("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb"),
        ("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb"),
    )
    for key, val in data:
        assert decode1(key) == val
        assert decode2(key) == val
        assert decode3(key) == val


if __name__ == '__main__':
    test()
