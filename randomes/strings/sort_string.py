"""
Определите метод, который принимает две строки в качестве параметров.
Метод возвращает первую строку, отсортированную по второй.

sort_string("foos", "of")       == "oofs"
sort_string("string", "gnirts") == "gnirts"
sort_string("banana", "abn")    == "aaabnn"

Чтобы уточнить, вторая строка определяет порядок. Вполне возможно,
что во второй строке символы повторяются, поэтому следует удалить
повторяющиеся символы, оставив только первое вхождение.

Любой символ в первой строке, который не встречается во второй строке,
должен быть отсортирован до конца результата в исходном порядке.
"""


def sort_string(st: str, order: str) -> str:
    """
    Сортирует первую строку по второй.
    """
    return ''.join(sorted(st, key=order[::-1].rfind, reverse=True))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("banana", "abn"), "aaabnn"),
        (("banana", "xyz"), "banana"),
        (("banana", "an"), "aaannb"),
        (("foos", "of"), "oofs"),
        (("string", "gnirts"), "gnirts"),
        (("banana", "a"), "aaabnn"),
        (("bungholio", "aacbuoldiiaoh"), "buoolihng"),
        (("fumyarhncujlj", "nsejcwn"), "njjcfumyarhul"),
    )
    for key, val in data:
        assert sort_string(*key) == val


if __name__ == '__main__':
    test()
