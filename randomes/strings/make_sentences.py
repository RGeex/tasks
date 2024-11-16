"""
Реализуйте функцию, чтобы она создавала предложение из заданных частей.

Массив частей может содержать:

    слова;
    запятые посередине;
    несколько периодов в конце.

Правила составления предложений:

    между словами всегда должен быть пробел;
    между запятой и словом слева не должно быть пробела;
    в конце предложения всегда должна быть одна и только одна точка.

Пример:

makeSentence(['hello', ',', 'my', 'dear']) // returns 'hello, my dear.'
"""


def make_sentences(parts: list[str]) -> str:
    """
    Обяединяет слова в предложение.
    """
    return ' '.join(parts).strip('. ').replace(' ,', ',') + '.'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (['hello', 'world'], 'hello world.'),
        (['Quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'], 'Quick brown fox jumped over the lazy dog.'),
        (['hello', ',', 'my', 'dear'], 'hello, my dear.'),
        (['one', ',', 'two', ',', 'three'], 'one, two, three.'),
        (['One', ',', 'two', 'two', ',', 'three', 'three', 'three', ',', '4', '4', '4', '4'], 'One, two two, three three three, 4 4 4 4.'),
        (['hello', 'world', '.'], 'hello world.'),
        (['Bye', '.'], 'Bye.'),
        (['hello', 'world', '.', '.', '.'], 'hello world.'),
        (['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 'The Earth rotates around The Sun in 365 days, I know that.'),
    )
    for key, val in data:
        assert make_sentences(key) == val


if __name__ == '__main__':
    test()
