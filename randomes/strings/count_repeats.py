"""
Напишите функцию, возвращающую количество символов, которые необходимо удалить,
чтобы получить строку без последовательных повторов.

Примечание. Сюда входят любые символы.
Примеры

'abbbbc'  => 'abc'    #  answer: 3
'abbcca'  => 'abca'   #  answer: 2
'ab cca'  => 'ab ca'  #  answer: 1

"""


from itertools import groupby as gb


def count_repeats(txt: str) -> int:
    """
    Поиск кол-ва подряд идущих повторов символов в строке.
    """
    return sum(len(list(x)) - 1 for _, x in gb(txt))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('abcdefg', 0),
        ('aabbccddeeffgg', 7),
        ('abcdeefee', 2),
        ('122453124', 1),
        ('@*$##^^^*)*', 3),
    )
    for key, val in data:
        assert count_repeats(key) == val


if __name__ == '__main__':
    test()
