"""
Во входной строке word(1 слово):

    замените гласную ближайшей левой согласной.
    замените согласную ближайшей правой гласной.

PS Чтобы выполнить это задание, представьте, что алфавит представляет собой
круг (соедините в уме первый и последний элемент массива). Например,
«a» замените на «z», «y» на «a» и т. д. (см. ниже).

Например:

'codewars' => 'enedazuu'
'cat' => 'ezu'
'abcdtuvwxyz' => 'zeeeutaaaaa'


PS Вы работаете только со строчными буквами.
"""


from functools import reduce


def replace_letters(word: str) -> str:
    """
    Заменяет буквы в слове, гласную на ближайшую согласную слева,
    согласную на ближайшую гласную справа, учитывая закольцованный алфавит.
    """
    key, val = 'a bcd e fgh i jklmn o pqrst u vwxyz'.split(), list('zedihonuta')
    x = reduce(lambda a, b: a | b, [{x: v for x in k} for k, v in zip(key, val)])
    return ''.join([x.get(w, '') for w in word])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('cat', 'ezu'),
        ('codewars', 'enedazuu'),
        ('abcdtuvwxyz', 'zeeeutaaaaa'),
    )
    for key, val in data:
        assert replace_letters(key) == val


if __name__ == '__main__':
    test()
