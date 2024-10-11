"""
Учитывая строку, содержащую буквенно-цифровые символы («3a4B2d»), верните
расширение этой строки: числовые значения представляют собой появление
каждой буквы, предшествующей этому числовому значению. В конечной строке
не должно быть цифровых символов.
Примечания

    Первое появление числового значения должно соответствовать количеству
    повторений каждого символа, стоящего за ним, до появления следующего
    числового значения.
    Если имеется несколько последовательных цифровых символов, следует
    использовать только последний (игнорируйте предыдущие).
    Пустые строки должны возвращать пустую строку.

Ваш код должен работать как с строчными, так и с заглавными буквами.

"3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
"3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
"3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
"abcde"     -->  "abcde"           # no digits
"1111"      -->  ""                # no characters to repeat
""          -->  ""                # empty string
"""


import re


def string_expansion(s: str) -> str:
    """
    Расширяет строку на кол-во символов указанное перед буквенным выражением.
    """
    x = re.split(r'(\d+)', s)
    return ''.join(x[:1] + [w for x in [[w * int(x[i][-1]) for w in x[i+1]] for i in range(1, len(x), 2)] for w in x])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('3D2a5d2f', 'DDDaadddddff'),
        ('4D1a8d4j3k', 'DDDDaddddddddjjjjkkk'),
        ('4D2a8d4j2f', 'DDDDaaddddddddjjjjff'),
        ('3n6s7f3n', 'nnnssssssfffffffnnn'),
        ('0d4n8d2b', 'nnnnddddddddbb'),
        ('0c3b1n7m', 'bbbnmmmmmmm'),
        ('7m3j4ik2a', 'mmmmmmmjjjiiiikkkkaa'),
        ('3A5m3B3Y', 'AAAmmmmmBBBYYY'),
        ('5M0L8P1', 'MMMMMPPPPPPPP'),
        ('2B', 'BB'),
        ('7M1n3K', 'MMMMMMMnKKK'),
        ('A4g1b4d', 'Aggggbdddd'),
        ('111111', ''),
        ('4d324n2', 'ddddnnnn'),
        ('5919nf3u', 'nnnnnnnnnfffffffffuuu'),
        ('2n1k523n4i', 'nnknnniiii'),
        ('6o23M32d', 'ooooooMMMdd'),
        ('1B44n3r', 'Bnnnnrrr'),
        ('M21d1r32', 'Mdr'),
        ('23M31r2r2', 'MMMrrr'),
        ('8494mM25K2A', 'mmmmMMMMKKKKKAA'),
        ('4A46D6B3C', 'AAAADDDDDDBBBBBBCCC'),
        ('23D42B3A', 'DDDBBAAA'),
        ('143D36C1A', 'DDDCCCCCCA'),
        ('asdf', 'asdf'),
        ('23jbjl1eb', 'jjjbbbjjjllleb'),
        ('43ibadsr3', 'iiibbbaaadddsssrrr'),
        ('123p9cdbjs', 'pppcccccccccdddddddddbbbbbbbbbjjjjjjjjjsssssssss'),
        ('2309ew7eh', 'eeeeeeeeewwwwwwwwweeeeeeehhhhhhh'),
        ('312987rfebd', 'rrrrrrrfffffffeeeeeeebbbbbbbddddddd'),
        ('126cgec', 'ccccccggggggeeeeeecccccc'),
        ('1chwq3rfb', 'chwqrrrfffbbb'),
        ('389fg21c', 'fffffffffgggggggggc'),
        ('239vbsac', 'vvvvvvvvvbbbbbbbbbsssssssssaaaaaaaaaccccccccc'),
        ('davhb327vuc', 'davhbvvvvvvvuuuuuuuccccccc'),
        ('cvyb239bved2dv', 'cvybbbbbbbbbbvvvvvvvvveeeeeeeeedddddddddddvv'),
        ('', ''),
    )
    for key, val in data:
        assert string_expansion(key) == val


if __name__ == '__main__':
    test()
