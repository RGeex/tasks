"""
В этом ката вам нужно создать функцию с именем insertMissingLetters, это
занимает string и выводит ту же строку, обработанную определенным образом.

Функция должна вставлять только после первого появления каждого символа
входной строки все буквы алфавита , которые:

- НЕ находятся в исходной строке
- идти после буквы обрабатываемой строки

Каждая добавленная буква должна находиться в uppercase, буквы исходной строки
всегда будут в lowercase.

Пример:

input: "holly"

missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"

output: "hiJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"

Вам не нужно проверять ввод, входная строка всегда будет содержать
определенное количество строчных букв (минимум 1/максимум 50).
"""


def insert_missing_letters(st: str) -> str:
    """
    Форматирует заданную строку согласно правилам.
    """
    return ''.join([w + ('' if w in st[:i] else ''.join([chr(x) for x in range(ord(w.upper()) + 1, 91) if chr(x) not in st.upper()])) for i, w in enumerate(st)])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("hello","hIJKMNPQRSTUVWXYZeFGIJKMNPQRSTUVWXYZlMNPQRSTUVWXYZloPQRSTUVWXYZ"),
        ("abcdefghijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz"),
        ("hellllllllllllooooo","hIJKMNPQRSTUVWXYZeFGIJKMNPQRSTUVWXYZlMNPQRSTUVWXYZllllllllllloPQRSTUVWXYZoooo"),
        ("pixxa","pQRSTUVWYZiJKLMNOQRSTUVWYZxYZxaBCDEFGHJKLMNOQRSTUVWYZ"),
        ("xpixax","xYZpQRSTUVWYZiJKLMNOQRSTUVWYZxaBCDEFGHJKLMNOQRSTUVWYZx"),
        ("z", "z"),
    )
    for key, val in data:
        assert insert_missing_letters(key) == val


if __name__ == '__main__':
    test()
