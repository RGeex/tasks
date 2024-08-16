"""
Учитывая строку, удалите из строки все уникальные символы.

Пример:

ввод: «abccdefee»

вывод: "cceee"
"""


def only_duplicates(st: str) -> str:
    """
    Удаляет из строки уникальные символы.
    """
    return ''.join(x for x in st if st.count(x) > 1)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('abccdefee', 'cceee'),
        ('hello', 'll'),
        ('colloquial', 'ollol'),
        ('foundersandcoders', 'ondersndoders'),
        ('12314256aaeff', '1212aaff'),
    )
    for key, val in data:
        assert only_duplicates(key) == val


if __name__ == '__main__':
    test()
