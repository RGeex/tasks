"""
Давайте говорить как обезьяны. Узнайте как! Посмотрите тестовые примеры и код инженера для их прохождения.
"""


def monkey_talk(s: str) -> str:
    """
    Переводит переданный текст в обезьяний язык.
    """
    return f"{' '.join(['ook', 'eek'][w[0] in 'aeiou'] for w in s.lower().split()).capitalize()}."


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('Hello', 'Ook.'),
        ('Everyone', 'Eek.'),
        ('Hello Everyone', 'Ook eek.'),
        ('Everyone Hello', 'Eek ook.'),
    )
    for key, val in data:
        assert monkey_talk(key) == val


if __name__ == '__main__':
    test()
