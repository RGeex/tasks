"""
Учитывая строку, выведите закодированную версию этой строки.
Пример:
Вход:

'When nobody is around, the trees gossip about the people who have walked
under them.'

Во-первых, входные данные нормализуются; Любые символы, кроме буквенных,
следует удалить из текста и перевести сообщение в нижний регистр. Будут
передаваться только английские алфавиты (верхние и строчные буквы) и
допустимые неалфавитные символы, т.е .:

!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

Никакие цифры не будут передаваться в качестве входных данных.
Входные данные нормализуются в:

'whennobodyisaroundthetreesgossipaboutthepeoplewhohavewalkedunderthem'

Затем текст организуется в прямоугольник размером (a * b) такой, что
b >= a и b - a <= 1. Последняя строка, если она неполная, должна быть
дополнена пробелами. Поскольку длина нормализованного текста равна 68,
мы используем прямоугольник 8*9;

'whennobod'
'yisaround'
'thetreesg'
'ossipabou'
'tthepeopl'
'ewhohavew'
'alkedunde'
'rthem    '

Окончательное сообщение получается путем чтения прямоугольника в каждом
столбце слева направо и разделения на b куски длины a, разделенные пробелами.
В выводе нельзя использовать никакие символы, кроме строчных букв английского
алфавита и пробелов.
Выход:

'wytotear hihstwlt eseshhkh natieoee nrrpphdm ooeaeau  buebovn  onsoped  ddgulwe ' 
"""


def cipher_text(s: str) -> str:
    """
    Шифрование строки.
    """
    s = __import__('re').sub(r'[^a-z]', '', s.lower())
    n = [x := (not (x := len(s) ** .5).is_integer()) + int(x), [x, x - 1][len(s) < (x - 1) * x]]
    return ' '.join(map(''.join, zip(*[f'{s[i*n[0]:i*n[0]+n[0]]:<{n[0]}}' for i in range(n[1])])))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('When nobody is around, the trees gossip about the people who have walked under them.','wytotear hihstwlt eseshhkh natieoee nrrpphdm ooeaeau  buebovn  onsoped  ddgulwe '),
        ('I want a giraffe, but I\'m a turtle eating waffles.','iiuril wrttne aailgs nfmew  tfaea  aetaf  gbutf ' ),
        ('Dolores wouldn\'t have eaten the meal if she had known what it actually was.','dovhsoty oueehwaw llemenca odaehwts rntaahu  eteldaa  shniktl  watfnil '),
        ('She says she has the ability to hear the soundtrack of your life.','shaoscl hebhoki ehieuof salanfe asirdy  ytttto  shyhru  setear '),
        ('I\'ve always wanted to go to Tajikistan, but my cat would miss me.','isoiuom vwgktue eaoiml  antsyd  ltotcm  wetaai  adants  ytjbws '),
        ('###',''),
    )
    for key, val in data:
        assert cipher_text(key) == val


if __name__ == '__main__':
    test()
