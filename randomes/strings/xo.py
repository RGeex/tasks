"""
Проверьте, содержит ли строка одинаковое количество «x» и «o».
Метод должен возвращать логическое значение и не учитывать регистр.
Строка может содержать любой символ.
"""

from operator import eq


def xo(s: str):
    """Поиск в строке 'x' и 'o', сравнение их колличеств."""
    return eq(*[s.lower().count(i) for i in 'xo'])


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ("", True),
        ("ooxx", True),
        ("oxOx", True),
        ("zzoo", False),
        ("ooxXm", True),
        ("xooxx", False),
        ("zpzpzpp", True),
    ]

    for string, value in data:
        assert xo(string) == value


if __name__ == '__main__':
    test()
