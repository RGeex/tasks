"""
Напишите функцию, которая принимает строку, состоящую только из букв ASCII и
пробелов, и возвращает эту строку печатными буквами шириной 5 символов и
высотой 7 символов с одним пробелом между символами.

Строка должна быть отформатирована таким образом, чтобы при передаче в Pythons
print() Функция показывает желаемый результат (см., например, ниже).

Существует предварительно загруженный словарь под названием ALPHA, который вы
можете использовать. Ключи — строчные буквы и пробел. Неудачные тесты
переформатируются для упрощения отладки с помощью предварительно загруженной
функции. unbleach().

    Печатные буквы должны состоять из соответствующих заглавных букв.
    Не имеет значения, состоит ли ввод из строчных или прописных букв.
    Любые начальные и/или конечные пробелы во входных данных следует
    игнорировать.
    Пустые строки или такие строки, содержащие только пробелы, должны
    возвращать пустую строку.
    Остальные пробелы (между буквами и/или словами) следует рассматривать
    как любой другой символ. Это означает, что на выходе будет шесть
    пробелов для пробела на входе или кратно шести, если пробелов было
    больше, плюс один из предыдущего символа!
    Конечные пробелы следует удалить в полученной строке
    (а также в ее подстроках!).
    Чтобы облегчить отладку, сообщения об ошибках тестирования искажают
    выходные данные: пробелы заменяются символом маркера. U+2022, а
    символы конца строки \n видны.

print(block_print('heLLo WorLD'))

должен привести к выводу, который выглядит следующим образом:

H   H EEEEE L     L      OOO        W   W  OOO  RRRR  L     DDDD
H   H E     L     L     O   O       W   W O   O R   R L     D   D
H   H E     L     L     O   O       W   W O   O R   R L     D   D
HHHHH EEEEE L     L     O   O       W W W O   O RRRR  L     D   D
H   H E     L     L     O   O       W W W O   O R R   L     D   D
H   H E     L     L     O   O       W W W O   O R  R  L     D   D
H   H EEEEE LLLLL LLLLL  OOO         W W   OOO  R   R LLLLL DDDD
"""


abc = {
    'a': [' AAA ', 'A   A', 'A   A', 'AAAAA', 'A   A', 'A   A', 'A   A'],
    'b': ['BBBB ', 'B   B', 'B   B', 'BBBB ', 'B   B', 'B   B', 'BBBB '],
    'c': [' CCC ', 'C   C', 'C    ', 'C    ', 'C    ', 'C   C', ' CCC '],
    'd': ['DDDD ', 'D   D', 'D   D', 'D   D', 'D   D', 'D   D', 'DDDD '],
    'e': ['EEEEE', 'E    ', 'E    ', 'EEEEE', 'E    ', 'E    ', 'EEEEE'],
    'f': ['FFFFF', 'F    ', 'F    ', 'FFFFF', 'F    ', 'F    ', 'F    '],
    'g': [' GGG ', 'G   G', 'G    ', 'G GGG', 'G   G', 'G   G', ' GGG '],
    'h': ['H   H', 'H   H', 'H   H', 'HHHHH', 'H   H', 'H   H', 'H   H'],
    'i': ['IIIII', '  I  ', '  I  ', '  I  ', '  I  ', '  I  ', 'IIIII'],
    'j': ['JJJJJ', '    J', '    J', '    J', '    J', '    J', 'JJJJ '],
    'k': ['K   K', 'K  K ', 'K K  ', 'KK   ', 'K K  ', 'K  K ', 'K   K'],
    'l': ['L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
    'm': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M', 'M   M', 'M   M'],
    'n': ['N   N', 'NN  N', 'N   N', 'N N N', 'N   N', 'N  NN', 'N   N'],
    'o': [' OOO ', 'O   O', 'O   O', 'O   O', 'O   O', 'O   O', ' OOO '],
    'p': ['PPPP ', 'P   P', 'P   P', 'PPPP ', 'P    ', 'P    ', 'P    '],
    'q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q   Q', 'Q Q Q', 'Q  QQ', ' QQQQ'],
    'r': ['RRRR ', 'R   R', 'R   R', 'RRRR ', 'R R  ', 'R  R ', 'R   R'],
    's': [' SSS ', 'S   S', 'S    ', ' SSS ', '    S', 'S   S', ' SSS '],
    't': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  ', '  T  ', '  T  '],
    'u': ['U   U', 'U   U', 'U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
    'v': ['V   V', 'V   V', 'V   V', 'V   V', 'V   V', ' V V ', '  V  '],
    'w': ['W   W', 'W   W', 'W   W', 'W W W', 'W W W', 'W W W', ' W W '],
    'x': ['X   X', 'X   X', ' X X ', '  X  ', ' X X ', 'X   X', 'X   X'],
    'y': ['Y   Y', 'Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  ', '  Y  '],
    'z': ['ZZZZZ', '    Z', '   Z ', '  Z  ', ' Z   ', 'Z    ', 'ZZZZZ'],
}


def block_print(s: str) -> str:
    """
    Печатает строку печатными буквами шириной 5 символов и
    высотой 7 символов с одним пробелом между символами.
    """
    return '\n'.join([' '.join(x).rstrip() for x in zip(*[abc.get(x, [' ' * 5] * 7) for x in s.lower().strip()])])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('heLLo WorLD', 'H   H EEEEE L     L      OOO        W   W  OOO  RRRR  L     DDDD\nH   H E     L     L     O   O       W   W O   O R   R L     D   D\nH   H E     L     L     O   O       W   W O   O R   R L     D   D\nHHHHH EEEEE L     L     O   O       W W W O   O RRRR  L     D   D\nH   H E     L     L     O   O       W W W O   O R R   L     D   D\nH   H E     L     L     O   O       W W W O   O R  R  L     D   D\nH   H EEEEE LLLLL LLLLL  OOO         W W   OOO  R   R LLLLL DDDD'),
        ('ABCDEFGHIJKLM', ' AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M\nA   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM\nA   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M\nAAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M\nA   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M\nA   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M\nA   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M'),
        ('NOPQRSTUVWXYZ', 'N   N  OOO  PPPP   QQQ  RRRR   SSS  TTTTT U   U V   V W   W X   X Y   Y ZZZZZ\nNN  N O   O P   P Q   Q R   R S   S   T   U   U V   V W   W X   X Y   Y     Z\nN   N O   O P   P Q   Q R   R S       T   U   U V   V W   W  X X   Y Y     Z\nN N N O   O PPPP  Q   Q RRRR   SSS    T   U   U V   V W W W   X     Y     Z\nN   N O   O P     Q Q Q R R       S   T   U   U V   V W W W  X X    Y    Z\nN  NN O   O P     Q  QQ R  R  S   S   T   U   U  V V  W W W X   X   Y   Z\nN   N  OOO  P      QQQQ R   R  SSS    T    UUU    V    W W  X   X   Y   ZZZZZ'),
        ('   same', ' SSS   AAA  M   M EEEEE\nS   S A   A MM MM E\nS     A   A M M M E\n SSS  AAAAA M   M EEEEE\n    S A   A M   M E\nS   S A   A M   M E\n SSS  A   A M   M EEEEE'),
        ('same   ', ' SSS   AAA  M   M EEEEE\nS   S A   A MM MM E\nS     A   A M M M E\n SSS  AAAAA M   M EEEEE\n    S A   A M   M E\nS   S A   A M   M E\n SSS  A   A M   M EEEEE'),
        ('   but   different   ', 'BBBB  U   U TTTTT                   DDDD  IIIII FFFFF FFFFF EEEEE RRRR  EEEEE N   N TTTTT\nB   B U   U   T                     D   D   I   F     F     E     R   R E     NN  N   T\nB   B U   U   T                     D   D   I   F     F     E     R   R E     N   N   T\nBBBB  U   U   T                     D   D   I   FFFFF FFFFF EEEEE RRRR  EEEEE N N N   T\nB   B U   U   T                     D   D   I   F     F     E     R R   E     N   N   T\nB   B U   U   T                     D   D   I   F     F     E     R  R  E     N  NN   T\nBBBB   UUU    T                     DDDD  IIIII F     F     EEEEE R   R EEEEE N   N   T'),
        ('  ', '')
    )
    for key, val in data:
        assert block_print(key) == val


if __name__ == '__main__':
    test()
