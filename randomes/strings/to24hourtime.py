"""
Преобразование 12-часового времени, такого как «8:30 утра» или
«20:30 вечера», в 24-часовое время (например, «08:30» или «20:30»)
звучит достаточно просто, не так ли? Что ж, посмотрим, сможешь ли
ты это сделать!

Вам нужно будет определить функцию, которой будет задан час
(всегда в диапазоне от 1 до 12 включительно), минута
(всегда в диапазоне от 0 до 59 включительно) и период
(либо «am», или "pm") в качестве входных данных.

Ваша задача — вернуть четырехзначную строку, которая кодирует это
время в 24-часовом формате.

Примечания
По соглашению полдень 12:00 pm, а полночь 12:00 am.
В 12-часовом формате нет 0 часов, а время сразу после полуночи обозначается,
например, как 12:15 am. В 24-часовом формате это означает 0015.
"""


def to24hourtime(hour, minute, period):
    """
    Преобразовывает 12-ти часовой формат в 24-х часовой по шаблону.
    """
    return ''.join(str(x).zfill(2) for x in (hour % 12 + {'pm': 12}.get(period, 0), minute))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """

    data = (
        ((1,  0, 'am'), '0100'),
        ((1,  0, 'pm'), '1300'),
        ((12,  0, 'am'), '0000'),
        ((12,  0, 'pm'), '1200'),
        ((6, 30, 'am'), '0630'),
        ((9, 45, 'pm'), '2145'),
    )
    for key, val in data:
        assert to24hourtime(*key) == val


if __name__ == '__main__':
    test()