"""
Преобразовать строку из букв в набор точек,
разделенных пробелами.

Таблица кодировки:

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z

Пример использования:

"D" = (1, 4) = ". ...."
"O" = (3, 4) = "... ...."
"T" = (4, 4) = ".... ...."
"""


def translation(text: str) -> str:
    """Замена буквенных символов строки на набор из точек,
    определенной последовательности."""

    def func(numbers: tuple) -> str:
        """Замена букв точками."""
        return ' '.join(map(lambda x: '.' * x, numbers))

    # буквы Английского алфавита
    chrs = list(map(chr, range(97, 123)))
    # словарь букв с точками
    data = {v: func((i//5+1, i % 5+1)) for i, v in enumerate(chrs[:10]+chrs[11:])}
    data['k'] = data['c']

    return ' '.join(map(data.get, text.lower()))


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ("taps", ".... .... . . ... ..... .... ..."),
        ("breaks", ". .. .... .. . ..... . . . ... .... ..."),
        ("knocks", ". ... ... ... ... .... . ... . ... .... ..."),
    ]

    for key, value in data:
        assert translation(key) == value


if __name__ == '__main__':
    test()
