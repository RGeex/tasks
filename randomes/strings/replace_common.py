"""
Найдите самую распространенную букву (не пробел) в string(всегда строчные
буквы и 2 < слова) и замените его на letter.

Если таких букв две и более, выберите ту, которая появится в string( ранее.

Например:

('my mom loves me as never did', 't') => 'ty tot loves te as never did'
('real talk bro', 'n') => 'neal talk bno'
('great job go ahead', 'k') => 'grekt job go khekd'
"""


def replace_common(st: str, letter: str) -> str:
    """
    Заменяет самый популярный символ, кроме пробела, на заданный символ.
    """
    return st.replace(max(st.replace(' ', ''), key=st.count), letter)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('my mom loves me as never did', 't'), 'ty tot loves te as never did'),
        (('real talk bro', 'n'), 'neal talk bno'),
        (('great job go ahead', 'k'), 'grekt job go khekd'),
        (('yyyaaa twwww ttt uuu ccca', 'p'), 'yyyppp twwww ttt uuu cccp'),
    )
    for key, val in data:
        assert replace_common(*key) == val


if __name__ == '__main__':
    test()
