"""
Сколько строк, равных A, можно составить из букв строки B?
Каждую букву можно использовать только один раз и только в одной строке.

Пример:
Для A = "abc" and B = "abccba", вывод должен быть 2.

Мы можем построить 2 строки A с письмами от B.

Строка, содержащая необходимые буквы, B
содержит только строчные английские буквы.
"""

from collections import Counter


def strings_construction(a: str, b: str) -> int:
    """
    Поиск колличеств комбинаций букв первой строки во второй,
    используя каждую букву только 1 раз.
    """
    a, b = map(Counter, (a, b))
    return min(b.get(k, 0) // v for k, v in a.items())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """

    data = (
        (("abc", "abccba"), 2),
        (("hnccv", "hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn"), 3),
        (("abc", "def"), 0),
        (("zzz", "zzzzzzzzzzz"), 3),
    )
    for key, val in data:
        assert strings_construction(*key) == val


if __name__ == '__main__':
    test()
