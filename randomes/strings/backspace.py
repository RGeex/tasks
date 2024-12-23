"""
Вам предоставляется string букв, которые вам нужно напечатать. В строке есть
специальная функция: [backspace]. Как только вы столкнетесь с [backspace],
вы удаляете символ прямо перед ним. Если нечего backspace , просто продолжай.
Вернуть финал string .

например oopp[backspace]s возвращаться oops (удалить букву р)

Прохождение:

тот
и
открыть
упс
открыть [backspace]
oops

например ooppp[backspace][backspace]s возвращаться oops (удалить обе буквы)

Прохождение:

тот
и
открыть
упс
упс
упс [backspace]
открыть [backspace]
oops

например a[backspace][backspace]ooppp[backspace][backspace]s возвращаться oops

Прохождение:

а
[ничего]
[ничего]
тот
и
открыть
упс
упс
упс [backspace]
открыть [backspace]
oops

Но есть поворот! [backspace][backspace][backspace] может появиться как
[backspace]*3 или даже [backspace]*2[backspace]

По сути, [backspace][backspace] ... [backspace] n times может появиться как
[backspace]*n (n может быть даже 1, но не меньше 1 ( [backspace]*0 не произойдет))

например a[backspace]*2oopppp[backspace]*2[backspace]s
возвращаться oops
"""


import re


def backspace(s: str) -> str:
    """
    Рекурсивно удаляет символ стоящий перед [backspace] в строке.
    """
    def calc(match: re.match) -> str:
        """
        Вычисляется строка для замены.
        """
        return f'{match.group(2)}*{x}' if (x := int(match.group(4) or 1) - 1) else ''

    return s if (r := re.sub(r'(^|[^\\\d\]])(\[backspace\])(\*?)(\d*)', calc, s)) == s else backspace(r)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('abcde[backspace]', 'abcd'),
        ('oopp[backspace]s', 'oops'),
        ('ooppp[backspace][backspace]s', 'oops'),
        ('[backspace]*1a', 'a'),
        ('ooppp[backspace]*2s', 'oops'),
        ('oop[backspace]*1oo[backspace]*2pppp[backspace]*3s', 'oops'),
        ('', ''),
        ('[backspace]', ''),
        ('[backspace]*3a  [backspace]', 'a '),
        ('No backspaces', 'No backspaces'),
    )
    for key, val in data:
        assert backspace(key) == val


if __name__ == '__main__':
    test()
