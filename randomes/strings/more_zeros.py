"""
Создайте функцию moreZeros , которая будет получать строку для ввода и
возвращать массив (или строку с нулевым завершением в C), содержащую
только символы из этой строки, двоичное представление ее значения
ASCII которого состоит из большего количества нулей, чем единиц.

Вам следует удалить все повторяющиеся символы , сохраняя первое вхождение
любых таких дубликатов, чтобы они располагались в конечном массиве в том
же порядке , в котором они впервые появились во входной строке.

Примеры

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False
                   
        --> ['a','b','d']
    
'DIGEST'--> ['D','I','E','T']

Все входные данные будут действительными строками длиной > 0. Ведущие нули в
двоичном формате не учитываются.
"""

from collections import Counter


def more_zeros(s: str) -> list[str]:
    """
    Выбирает из строки символы встречающиеся впервые и имеющие
    больше половины 1 чем 0 в побитовом представлении.
    """
    return sorted({w for w in s if not int(max(Counter(f'{ord(w):b}').items(), key=lambda x: x[1])[0])}, key=s.index)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('abcde', ['a', 'b', 'd']),
        ('thequickbrownfoxjumpsoverthelazydog', ['h', 'b', 'p', 'a', 'd']),
        ('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG', ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D']),
        ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_', ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0']),
        ('DIGEST', ['D', 'I', 'E', 'T']),
        ('abcdabcd', ['a', 'b', 'd']),
        ('Forgiveness is the fragrance that the violet sheds on the heal that has crushed it', ["F", " ", "h", "a", "d"]),
    )
    for key, val in data:
        assert more_zeros(key) == val


if __name__ == '__main__':
    test()
