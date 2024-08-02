"""
Вам дана последовательность допустимых слов и строка. Проверьте, состоит ли
строка из одного или нескольких слов из массива.
Задача

Проверьте, может ли строка быть полностью сформирована путем последовательного
объединения слов словаря.

Например:

dictionary: ["code", "wars"]

s1:         "codewars" =>  true  -> match 'code', 'wars'
s2:         "codewar"  =>  false -> match 'code', unmatched 'war'

Одно слово из словаря можно использовать несколько раз.
"""


def valid_word(seq: list[str], word: str) -> bool:
    """
    Проверяет, возможно ли составить слово из ключей слвоваря.
    """
    for i in range(1, len(word) + 1):
        if word[:i] in seq:
            if valid_word(seq, word[i:]):
                return True
    return not word


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((['code', 'wars'], 'codewars'), True),
        ((['wars', 'code'], 'codewars'), True),
        ((['code', 'wars'], 'codecodewars'), True),
        ((['code', 'wars'], 'codewar'), False),
        ((['code', 'wars'], 'codewarscode'), True),
        ((['code', 'star', 'wars'], 'starwars'), True),
        ((['Star', 'Code', 'Wars'], 'StarCodeWars'), True),
        ((['Star', 'Code', 'Wars'], 'WarsStarCode'), True),
        ((['Star', 'Code', 'Wars'], 'CodeStarsWar'), False),
        (([], 'codewars'), False),
        ((['code', 'wars'], 'code'), True),
        ((['a', 'b', 'c', 'd', 'e', 'f'], 'abcdef'), True),
        ((['a', 'b', 'c', 'd', 'e', 'f'], 'abcdefg'), False),
        ((['ab', 'a', 'bc'], 'abc'), True),
        ((['ab', 'bc'], 'abc'), False),
    )
    for key, val in data:
        assert valid_word(*key) == val


if __name__ == '__main__':
    test()
