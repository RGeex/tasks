"""
Для вас это очень простая задача!

Вам необходимо создать метод, который будет исправлять заданную строковую дату. Кроме того,
возникла проблема, из-за чего многие строки с датами оказались повреждены. Формат даты —
европейский. Это означает "ДД.ММ.ГГГГ".

Несколько примеров:

"30.02.2016" -> "01.03.2016"
"40.06.2015" -> "10.07.2015"
"11.13.2014" -> "11.01.2015"
"99.11.2010" -> "07.02.2011"

Если входная строка равна null или пуста, верните именно это значение!
Если формат строковой даты недопустим, вернуть null.

Подсказка: Сначала исправьте месяц, а затем день!

Получайте удовольствие от программирования и, пожалуйста, не забудьте проголосовать и оценить
это задание! :-)

"""
import unittest
from typing import Any, Callable, Tuple
import re
from datetime import datetime as dt, timedelta as td


def date_correct(date: str) -> str:
    """
    Испраляет значения даты, если она указана не верно.
    """
    if re.match(r'^\d{2}\.\d{2}\.\d{4}$', date or ''):
        d, m, y = map(int, date.split('.'))
        while True:
            if m > 12:
                m, y = m % 12, y + m // 12
            if d > (x := (dt([y + 1, y][m < 12], [1, m + 1][m < 12], 1) - td(days=1)).day):
                d, m = d - x, m + 1
                continue
            break
        return dt(y, m, d).strftime('%d.%m.%Y')
    return [None, ''][date == '']


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(date_correct, (
        (None, None),
        ("", ""),
        ("01112016", None),
        ("01,11,2016", None),
        ("0a.1c.2016", None),
        ("03.12.2016", "03.12.2016"),
        ("30.02.2016", "01.03.2016"),
        ("40.06.2015", "10.07.2015"),
        ("11.13.2014", "11.01.2015"),
        ("33.13.2014", "02.02.2015"),
        ("99.11.2010", "07.02.2011"),
        ("19.97.2064", "19.01.2072"),
    ))
