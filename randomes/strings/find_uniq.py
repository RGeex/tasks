"""
Есть массив строк. Все строки содержат одинаковые буквы, кроме одной.
Попробуйте найти его!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Строки могут содержать пробелы. Пробелы не имеют значения, имеют значение
только символы, не являющиеся пробелами. Например, строка, содержащая только
пробелы, аналогична пустой строке.

Гарантируется, что массив содержит более двух строк.
"""


def find_uniq(arr: list[str]) -> str:
    """
    Поиск строки в списке с неповторяющимися символами.
    """
    tmp = {}
    for i, s in enumerate(arr):
        for x in set(s.lower()):
            tmp[x] = tmp.get(x, [])
            tmp[x].append(i)

    return next(arr[x[0]] for x in tmp.values() if len(x) == 1)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'], 'BbBb'),
        (['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'], 'foo'),
        (['silvia', 'vasili', 'victor'], 'victor'),
        (['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter'], 'Harry Potter'),
        (['', '', '', 'a', '', ''], 'a'),
        (['    ', '  ', ' ', 'a', ' ', ''], 'a'),
        (['foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab'], '   '),
    )
    for key, val in data:
        assert find_uniq(key) == val


if __name__ == '__main__':
    test()
