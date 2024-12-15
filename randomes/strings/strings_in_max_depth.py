"""
Учитывая сбалансированную строку с скобками типа: «AA(XX((YY))(U))» найдите
подстроки,
заключенные в наибольшую глубину .

Пример:
String:  A   A   (   X   X   (   (   Y   Y   )   )   (   U   )   )
Level:        1        2  3       3  2  2    2  1

Поэтому ответьте: {"YY"}, так как подстрока "YY" заблокирована на самом
глубоком уровне .
Если на самом глубоком уровне находятся несколько подстрок, верните их все в
списке в порядке появления.

Строка включает только буквы верхнего регистра и круглые скобки «(» и «)».
Если входные данные пусты или не содержат скобок, должен быть возвращен массив,
содержащий только исходную строку.
"""


def strings_in_max_depth(s: str) -> list[str]:
    """
        Выполняет поиск максимальной глубины сложения скобок.
        """
    def wrap(s: str, n: int = 0, t: dict = {}) -> list[str]:
        """
        Обертка для изменяемого типа данных в контексте.
        """
        a, b, p, r = 0, 0, 0, []
        for i, x in enumerate(s):
            if x == '(':
                a, b, p = a + 1, 1, [p, i + 1][not b]
            if x == ')':
                a, (b, r) = a - 1, [(b, r + []), (0, r + [s[p:i]])][b and not a - 1]
        t[n] = t.get(n, []) + [[wrap(z, n + 1) for z in r] and [], [s]][not r]
        return max(t.items())[1]
    return wrap(s)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("AA(XX((YY))(U))", ["YY"]),
        ("((AAX(AB)(UP)F(Z))(HH))",  ['AB', 'UP', 'Z']),
        ("FB(TAIHJK(NZZCGDZXKF(SYMBLACQ)SBJMRFM)PRTRX(JCLYCOXIMOKGGIE)MWIOIJDCLXDSQFHK)WLVYSMNNHIGKR(MOIZLOT(RWMAVXSJQROHJ(GZURPPOQJVMYCE(VCPXSHXQ)LETIEWE(CBC)AAHEEO)NZHIGXBSJATXV)BSBYCMKFFAFZIK(KECNRQ)PIIQZGIDMLNQRQS)VGXXBYD", ['VCPXSHXQ', 'CBC']),
        ("AAA", ["AAA"]),
        ("", [""]),
    )
    for key, val in data:
        assert strings_in_max_depth(key) == val


if __name__ == '__main__':
    test()
