"""
Напишите две функции, которые преобразуют римскую цифру в целочисленное значение и обратно.
Для каждой функции будут проверены несколько значений римских цифр.

Современные римские цифры записываются путем выражения каждой цифры отдельно, начиная с
самой левой цифры и пропуская любую цифру со значением ноль. Римскими цифрами:

    1990отображается: 1000= M, 900= CM, 90= XC; в результате чего MCMXC
    2008написано как 2000= MM, 8= VIII; или MMVIII
    1666использует каждый римский символ в порядке убывания: MDCLXVI.

Диапазон ввода: 1 <= n < 4000

В этой ката 4должен быть представлен как IV, НЕ как IIII(«четверка часовщиков»).
Примеры

to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1

Помощь

+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+
"""


class RomanNumerals:
    """
    Взаимодействие римской и арабской системы счислений (ограничение n < 4000).
    """
    x1 = 'I IV V IX X XL L XC C CD D CM M'.split()
    x2 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    @staticmethod
    def to_roman(num: int) -> str:
        """
        Переводит арабское число в римское.
        """
        tmp = dict(zip(RomanNumerals.x2[::-1], RomanNumerals.x1[::-1]))
        val = next(((num := num - k) and v or v for k, v in tmp.items() if num >= k), '')
        return val + (RomanNumerals.to_roman(num) if val else '')

    @staticmethod
    def from_roman(num: str) -> int:
        """
        Переводит римское число в арабское
        """
        tmp = dict(zip(RomanNumerals.x1[::-1], RomanNumerals.x2[::-1]))
        val = next(((num := num.replace(k, '', 1)) and v or v for k,
                   v in tmp.items() if num.startswith(k)), 0)
        return val + (RomanNumerals.from_roman(num) if val else 0)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data1 = (
        (1000, 'M'),
        (4, 'IV'),
        (1, 'I'),
        (1990, 'MCMXC'),
        (2008, 'MMVIII'),
    )
    for key, val in data1:
        assert RomanNumerals.to_roman(key) == val

    data2 = (
        ('XXI', 21),
        ('I', 1),
        ('IV', 4),
        ('MMVIII', 2008),
        ('MDCLXVI', 1666),
    )
    for key, val in data2:
        assert RomanNumerals.from_roman(key) == val


if __name__ == '__main__':
    test()
