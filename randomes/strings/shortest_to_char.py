"""
Учитывая строку s и персонаж c, возвращает массив целых чисел, представляющих
кратчайшее расстояние от текущего символа в s к c.
Примечания

    Все буквы будут строчными.
    Если строка пуста, верните пустой массив.
    Если символ отсутствует, верните пустой массив.

Примеры

s = "lovecodewars"
c = "e"
result = [3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4]

s = "aaaabbbb"
c = "b"
result = [4, 3, 2, 1, 0, 0, 0, 0]

s = ""
c = "b"
result = []

s = "abcde"
c = ""
result = []
"""


def shortest_to_char(s: str, c: str) -> list[int]:
    """
    Находит расстояние до ближайшего заданного символа от текущей позиции.
    """
    return [min(next((i for i, x in enumerate(s[i::x or -1]) if c == x), float('inf')) for x in range(2)) for i in range(len(s))] if c and c in s else []


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("lovecodewars", "e"), [3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4]),
        (("aaaaa", "a"), [0, 0, 0, 0, 0]),
        (("aabbaabb", "a"), [0, 0, 1, 1, 0, 0, 1, 2]),
        (("aaaabbbb", "b"), [4, 3, 2, 1, 0, 0, 0, 0]),
        (("aaaaa", "b"), []),
        (("lovecoding", ""), []),
        (("", ""), []),
    )
    for key, val in data:
        assert shortest_to_char(*key) == val


if __name__ == '__main__':
    test()
