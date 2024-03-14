"""
Ваша задача для выполнения этого Ката — написать функцию, которая форматирует продолжительность,
заданную в секундах, удобным для человека способом.

Функция должна принимать неотрицательное целое число. Если он равен нулю, он просто возвращает "now".
В противном случае продолжительность выражается как комбинация years, days, hours, minutesи seconds.

Гораздо проще понять на примере:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"

Для целей этой Ката год состоит из 365 дней, а день — из 24 часов.

Обратите внимание, что пробелы важны.
Подробные правила

Полученное выражение состоит из таких компонентов, как 4 seconds, 1 yearи т. д.
Обычно положительное целое число и одна из допустимых единиц времени, разделенных пробелом.
Единица времени используется во множественном числе, если целое число больше 1.

Компоненты разделяются запятой и пробелом ( ", "). За исключением последнего компонента,
который отделяется " and ", так же, как это было бы написано на английском языке.

Более значимые единицы времени наступят раньше, чем наименее значимые. Поэтому, 1 second and 1 year
это не правильно, но 1 year and 1 secondявляется.

Разные компоненты имеют разную единицу измерения времени. Таким образом, здесь нет повторяющихся единиц,
как в 5 seconds and 1 second.

Компонент вообще не появится, если его значение равно нулю. Следовательно, 1 minute and 0 seconds
недействительно, но это должно быть просто 1 minute.

Единицу времени необходимо использовать «насколько это возможно». Это означает, что функция не
должна возвращать 61 seconds, но 1 minute and 1 secondвместо. Формально длительность, указанная в
компоненте, не должна превышать любую допустимую более значимую единицу времени.

"""

from operator import mul
from functools import reduce


def format_duration(n: int) -> str:
    """
    Преобразует секунды в кол-во времени в человеко-читаемый формат.
    """
    r, c, y = [], [60, 60, 24, 365], 'year day hour minute second'.split()
    for i in range(5):
        x, n = divmod(n, reduce(mul, c[:-i or None])) if i < 4 else (n, None)
        r.append(x)
    x = [f"{k} {v + ['', 's'][1 < k]}" for k, v in zip(r, y) if k]
    return ', '.join(x)[::-1].replace(' ,', ' dna ', 1)[::-1] or 'now'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (0, "now"),
        (1, "1 second"),
        (62, "1 minute and 2 seconds"),
        (120, "2 minutes"),
        (3600, "1 hour"),
        (3662, "1 hour, 1 minute and 2 seconds"),
        (15731080, "182 days, 1 hour, 44 minutes and 40 seconds"),
        (132030240, "4 years, 68 days, 3 hours and 4 minutes"),
        (205851834, "6 years, 192 days, 13 hours, 3 minutes and 54 seconds"),
        (253374061, "8 years, 12 days, 13 hours, 41 minutes and 1 second"),
        (242062374, "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"),
        (101956166, "3 years, 85 days, 1 hour, 9 minutes and 26 seconds"),
        (33243586, "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"),
    )
    for key, val in data:
        assert format_duration(key) == val


if __name__ == '__main__':
    test()
