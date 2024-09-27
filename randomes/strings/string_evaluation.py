"""
Оцените данную строку с заданными условиями.

Условия будут переданы в массиве и будут отформатированы следующим образом:

{symbol or digit}{comparison operator}{symbol or digit}

Верните результаты в массив.

Символы в условиях всегда будут находиться в строке. Символы в строке
выбираются из букв ascii + @#$%^&*()_{}[]
Пример

input string: "aab#HcCcc##l#"
conditions: ["a<b", "#==4", "c>=C", "H!=a"]

Условия в этом примере массива можно интерпретировать как:

    "a<b": количество раз "a" встречается в строке должно быть меньше, чем
    количество раз "b" встречается в строке
    "#==4": "#" должно встречаться ровно 4 раза в строке
    "c>=C": "c" должно произойти больше или равно числу раз "C" происходит
    "H!=a": количество раз "H" происходит не должно равняться количеству раз
    "a" происходит

В этом примере условие 1 false и 2, 3, 4 true. Таким образом, возвращаемое
значение будет массивом как таковым:

[False, True, True, True]
"""


import re
from operator import lt, le, eq, ne, ge, gt


def string_evaluation_1(s: str, c: list[str]) -> list[bool]:
    """
    Поиск в строке заданного щаблона.
    """
    f = dict(zip('<= == != >= < >'.split(), [le, eq, ne, ge, lt, gt]))
    return [f[re.search(rf'{"|".join(f)}', x).group()](*[int(w) if w.isdigit() else s.count(w) for w in re.split(rf'{"|".join(f)}', x)]) for x in c]


def string_evaluation_2(s: str, c: list[str]) -> list[bool]:
    """
    Поиск в строке заданного щаблона.
    """
    return [eval(''.join([e if i == 1 else e if e.isdigit() else str(s.count(e)) for i, e in enumerate(re.split(r'(<=|==|!=|>=|<|>)', x))])) for x in c]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('aab#HcCcc##l#', ['a<b', '#==4', 'c>=C', 'H!=a']), [False, True, True, True]),
        (('abc#$%KDAyyaa@@@', ['#>@', 'A==2', 'a>A', '$!=2']), [False, False, True, True]),
        (('abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1']), [False, False, False, True, False, True, False]),
    )
    for key, val in data:
        assert string_evaluation_1(*key) == val
        assert string_evaluation_2(*key) == val


if __name__ == '__main__':
    test()
