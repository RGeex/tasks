"""
Вы весь день собирали мелочь, и она начинает накапливаться в вашем кармане, но вам лень посмотреть,
сколько вы нашли.

Хорошо, что ты умеешь программировать!

Дополните функцию, чтобы она возвращала сумму сдачи в долларах!

К допустимым типам изменений относятся:

penny: 0.01
nickel: 0.05
dime: 0.10
quarter: 0.25
dollar: 1.00

Эти суммы уже предварительно загружены в виде плавающих средств. CHANGE словарь для вашего удобства!

Вы должны вернуть итоговую сумму в формате... $x.xx.

Примеры:

"nickel penny dime dollar" --> "$1.16"
"dollar dollar quarter dime dime" --> "$2.45"
"penny" --> "$0.01"
"dime" --> "$0.10"

Внимание! Сумма некоторых изменений может превышать указанную. $10.00!


"""
import unittest
from typing import Any, Callable, Tuple


CHANGE = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25, 'dollar': 1.0}


def change_count(change: str) -> str:
    """
    Подсчитывае сумму найденных монет в $.
    """
    return f'${sum(map(CHANGE.get, change.split())):.2f}'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(change_count, (
        ('dime penny dollar', '$1.11'),
        ('dime penny nickel', '$0.16'),
        ('quarter quarter', '$0.50'),
        ('dollar penny dollar', '$2.01'),
        ('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny', '$10.01'),
    ))
