"""
У пиратов печально известные трудности с произношением. Они склонны смешивать
все буквы вместе и кричать на людей.

Наконец-то нам нужен способ расшифровать то, что говорят эти пираты.

Напишите функцию, которая будет принимать как набор букв, так и словарь, и
выводить список слов, которые мог иметь в виду пират.

Например:

grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )

Должен вернуться ["sport", "ports"].

Возвращает совпадения в том же порядке, что и в словаре. Верните пустой массив,
если совпадений нет.
"""


def grabscrab(said: str, possible_words: list[str]) -> list[str]:
    """
    Поиск всех аннаграм, переданного слова, в переданном списке.
    """
    return [s for s in possible_words if sorted(s) == sorted(said)]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("trisf", ["first"]), ["first"]),
        (("oob", ["bob", "baobab"]), []),
        (("ainstuomn", ["mountains", "hills", "mesa"]), ["mountains"]),
        (("oolp", ["donkey", "pool", "horse", "loop"]), ["pool", "loop"]),
        (("ortsp", ["sport", "parrot", "ports", "matey"]), ["sport", "ports"]),
        (("ourf", ["one", "two", "three"]), []),
        (("racer", ["crazer", "carer", "racar", "caers", "racer"]), ["carer", "racer"]),
        (("abba", ["aabb", "abcd", "bbaa", "abbb", "aaab"]), ["aabb", "bbaa"]),
    )
    for key, val in data:
        assert grabscrab(*key) == val


if __name__ == '__main__':
    test()
