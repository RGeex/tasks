"""
Преобразовать строку в число.

Дана строка, в которой словами написано число, необходимо
преобразовать ее в числовое представление.

Язык слов: Английский, диапазон: от 0 до 1_000_000 включительно.
"""


def parse_int(string: str):
    """Преобразование строки в число."""

    ref = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
        'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
    }
    mult = {'hundred': 100, 'thousand': 1000, 'million': 1000000}

    res, tmp = 0, 0

    for num in string.split():
        if (mlt := mult.get(num)):
            var = mlt if mlt * tmp > res or not tmp else 1
            res = res * var + tmp * mlt
        tmp = sum(ref.get(n, 0) for n in num.split('-'))

    return res + tmp


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ('two hundred forty-six', 246),
        ('seven hundred thousand', 700000),
        ('two hundred three thousand', 203000),
        ('twenty-six thousand three hundred fifty-nine', 26359),
    ]

    for k, v in data:
        assert parse_int(k) == v


if __name__ == '__main__':
    test()
