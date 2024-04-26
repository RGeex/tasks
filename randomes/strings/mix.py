"""
Имея две строки s1 и s2, мы хотим визуализировать, насколько эти две строки различаются. Мы будем учитывать только строчные буквы (от а до z). Сначала посчитаем частоту встречаемости каждой строчной буквы в s1 и s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

Таким образом, максимум для «a» в s1 и s2 равен 4 из s1; максимум для 'b'
равен 3 от s2. В дальнейшем мы не будем рассматривать буквы, когда максимум
их вхождений меньше или равно 1.

Мы можем возобновить различия между s1 и s2 в следующей строке: "1:aaaa/2:bbb"
где 1в 1:aaaaобозначает строку s1 и aaaaпотому что максимум для aэто 4. Таким
же образом 2:bbbобозначает строку s2 и bbbпотому что максимум для bэто 3.

Задача состоит в том, чтобы создать строку, в которой каждая строчная буква s1
или s2 встречается столько раз, сколько его максимум, если этот максимум строго
больше 1 ; перед этими буквами будет стоять номер строки, в которой они
появляются с максимальным значением и :. Если максимум находится в s1, а также в
s2, префикс равен =:.

В результате подстроки (например, подстрока 2:nnnnn или 1:hhh; она содержит
префикс) будут располагаться в порядке убывания своей длины, а при одинаковой
длине - в возрастающем лексикографическом порядке (буквы и цифры - подробнее
точно отсортировано по коду); разные группы будут разделены символом «/». См.
примеры и «Примеры тестов».

Надеюсь, другие примеры смогут прояснить это.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

Примечание для Swift, R, PowerShell

Префикс =:заменяется на E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"
"""


from collections import Counter


def mix(s1: str, s2: str) -> str:
    """
    Из 2-х переданных строк формирует новую по заданному шаблону.
    """
    r, tmp = [], [{k: v for k, v in Counter(filter(str.islower, s)).items() if 1 < v} for s in (s1, s2)]

    for x in {*tmp[0], *tmp[1]}:
        a, b = [n.get(x, 0) for n in tmp]
        z = {a == b: 2, b < a: 0}.get(1, 1)
        r.append(('12='[z], x * tmp[z % 2][x]))

    return '/'.join(map(':'.join, sorted(r, key=lambda x: (-len(x[1]), x))))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr"),
        (("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'),
        (("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"),
        ((" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"),
        (("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo"),
        (("codewars", "codewars"), ""),
        (("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"),
    )
    for key, val in data:
        assert mix(*key) == val


if __name__ == '__main__':
    test()
