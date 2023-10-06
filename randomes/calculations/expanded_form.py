"""
Вам будет присвоен номер, и вам нужно будет вернуть его в виде строки в расширенной форме . Например:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

ПРИМЕЧАНИЕ. Все числа будут целыми числами больше 0. 
"""


def expanded_form(n: int) -> str:
    return ' + '.join(f'{int(x) * (10 ** abs(i))}' for i, x in enumerate(str(n), -len(str(n)) + 1) if int(x))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (12, '10 + 2'),
        (42, '40 + 2'),
        (70304, '70000 + 300 + 4'),
    )
    for key, val in data:
        assert expanded_form(key) == val


if __name__ == '__main__':
    test()
