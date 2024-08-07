"""
Вам будет предоставлен массив строк. Слова в массиве должны сцепляться друг с
другом, при этом одна или несколько букв в конце одного слова будут иметь те
же буквы (в том же порядке), что и следующее слово в массиве. Но бывают случаи,
когда все слова не совпадают.

Примеры смешанных слов:

«применить» и «фанера»

«яблоко» и «каждый»

«бегемот» и «мама»

Примеры слов, которые не совпадают:

«применить» и «детская площадка»

«яблоко» и «Пегги»

«бегемот» и «математика»

Если все слова в данном массиве связаны друг с другом, то ваш код должен
возвращать смешанные буквы в строке. Вы должны вернуть самую длинную общую
подстроку. Вы не будете знать, сколько букв общего у этих слов, но это будет
хотя бы одна.

Если какая-либо пара последовательных слов не может связаться, ваш код должен
вернуть «не удалось связать».

Входные данные: массив строк. Во входном массиве всегда будет как минимум два
слова.

Вывод: либо строка букв, объединяющая слова, либо строка "failed to mesh".
Примеры

#1:

["allow", "lowering", "ringmaster", "terror"] --> "lowringter"

потому что:

    письма "low" первые два слова сливаются воедино
    письма "ring" во втором и третьем слове сливаются воедино
    письма "ter" в третьем и четвертом словах сливаются воедино.

#2:

["kingdom", "dominator", "notorious", "usual", "allegory"] --> "failed to mesh"

Хотя слова "dominator" и "notorious" Распределяйте буквы в одном и том же
порядке, последние буквы первого слова не совпадают с первыми буквами второго слова.
"""


def word_mesh(words: list[str]) -> str:
    """
    Из связи слов формирует новое слово, либо сообщает что это невозможно.
    """
    x = [next((a[i:] for i in range(len(a)) if b.startswith(a[i:])), '') for a, b in zip(words, words[1:])]
    return all(x) and ''.join(x) or 'failed to mesh'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["beacon", "condominium", "umbilical", "california"], "conumcal"),
        (["allow", "lowering", "ringmaster", "terror"], "lowringter"),
        (["abandon", "donation", "onion", "ongoing"], "dononon"),
        (["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"], "ownhippuscartpher"),
    )
    for key, val in data:
        assert word_mesh(key) == val


if __name__ == '__main__':
    test()
