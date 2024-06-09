"""
На фабрике принтер печатает этикетки для коробок. В принтере используются
цвета, которые для простоты названы буквами от a до z
(кроме букв u, w, x или z это за ошибки).

Цвета, используемые принтером, записываются в управляющую строку. Например,
управляющая строка будет такой: aaabbbbhaijjjm это означает, что принтер
использовал три раза цвет a, четыре раза цвет b, один раз цвет h,
один раз цвет a... и так далее.

Иногда возникают проблемы: отсутствие цветов, техническая неисправность и
выдается контрольная строка, например uuaaaxbbbbyyhwawiwjjjwwxym где ошибки
обозначаются буквами u, w, x или z.

Вам нужно написать функцию hist который, учитывая строку, выведет ошибки в
виде строки, представляющей гистограмму обнаруженных ошибок.

Формат выходной строки:

буква (буквы ошибок сортируются в алфавитном порядке) в поле из 2 символов,
пробел, номер ошибки для этой буквы в поле из 6, столько «*», сколько ошибок
для этой буквы, и «\r» " (или "\n" в зависимости от языка).

Строка имеет длину большую или равную единице и содержит только буквы из a к z.
Примеры

s="uuaaaxbbbbyyhwawiwjjjwwxym"
hist(s) => "u  2     **\rw  5     *****\rx  2     **"

или с точками, чтобы увидеть пробелы:

hist(s) => "u..2.....**\rw..5.....*****\rx..2.....**"
s="uuaaaxbbbbyyhwawiwjjjwwxymzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
hist(s) => "u..2.....**\rw..5.....*****\rx..2.....**\rz..31....*******************************"

Примечания

    К сожалению, чаще всего Codewars сжимает все пробелы в одно.
    Другие примеры смотрите в разделе «Примеры тестов».


"""


import re
from collections import Counter


def hist(s: str) -> str:
    """
    Из заданной строки входных данных принтера, формируется строка ошибок, заданного формата.
    """
    return '\r'.join([f'{a:<3}{b:<6}{"*"*b}' for a, b in sorted(Counter(re.sub(r'[^uwxz]', '', s)).items())])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            "tpwaemuqxdmwqbqrjbeosjnejqorxdozsxnrgpgqkeihqwybzyymqeazfkyiucesxwutgszbenzvgxibxrlvmzihcb",
            "u  3     ***\rw  4     ****\rx  6     ******\rz  6     ******",
        ),
        (
            "aaifzlnderpeurcuqjqeywdq",
            "u  2     **\rw  1     *\rz  1     *",
        ),
        (
            "sjeneccyhrcpfvpujfaoaykqllteovskclebmzjeqepilxygdmzvdfmxbqdzubkzturnuqxsewrwgmdfwgdx",
            "u  4     ****\rw  3     ***\rx  4     ****\rz  4     ****",
        ),
        (
            "bnxyytdtqrkeaswymiwbxnuydwthweyzny",
            "u  1     *\rw  4     ****\rx  2     **\rz  1     *",
        ),
        (
            "tpaemqdmqbqrjbeosjnejqordosnrgpgqkeihqybyymqeafkyicestgsbenvgibrlvmihcb",
            "",
        ),
    )
    for key, val in data:
        assert hist(key) == val


if __name__ == '__main__':
    test()
