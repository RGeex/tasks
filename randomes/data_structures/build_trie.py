"""
Целью этого ката является реализация дерева префиксов (или дерева префиксов)
с использованием словарей (также известных как хэш-карты или хеш-таблицы), где:

    ключи словаря — это префиксы
    значение листового узла равно Noneна Питоне, nilв Руби, nullв Groovy, JavaScript и Java,
    а также Nothingв Хаскеле.
    значение для пустого ввода равно {}на Python, Ruby, Javascript и Java (пустая карта),
    [:]в Groovy и Trie []в Хаскеле.

Примеры:

>>> build_trie()
{}
>>> build_trie("")
{}
>>> build_trie("trie")
{'t': {'tr': {'tri': {'trie': None}}}}
>>> build_trie("tree")
{'t': {'tr': {'tre': {'tree': None}}}}
>>> build_trie("A","to", "tea", "ted", "ten", "i", "in", "inn")
{'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}}
>>> build_trie("true", "trust")
{'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}}

"""


def build_trie(*words: str) -> dict:
    """
    Создает дерево префиксов.
    """
    res = {}
    for word in words:
        p = res
        for i in range(len(word)):
            w = word[:i+1]
            p[w] = p.get(w) or (None if w == word else {})
            p = p[w]
    return res


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (tuple(), {}),
        (("", ), {}),
        (
            ("trie",),
            {'t': {'tr': {'tri': {'trie': None}}}},
        ),
        (
            ("tree",),
            {'t': {'tr': {'tre': {'tree': None}}}},
        ),
        (
            ("trie", "trie"),
            {'t': {'tr': {'tri': {'trie': None}}}},
        ),
        (
            ("A", "to", "tea", "ted", "ten", "i", "in", "inn"),
            {'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}},
                'i': {'in': {'inn': None}}},
        ),
        (
            ("true", "trust"),
            {'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}},
        ),
    )
    for key, val in data:
        assert build_trie(*key) == val


if __name__ == '__main__':
    test()
