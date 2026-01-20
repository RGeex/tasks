"""
Учитывая текущий обменный курс доллара США к евро, равный 1,1363636, напишите функцию,
которая будет принимать в качестве возвращаемого значения тип валюты и список сумм,
которые необходимо конвертировать.

Не забудьте, что это валюта, поэтому результат нужно будет округлить до второго знака после запятой.

Формат возврата в долларах США должен быть следующим: '$100,000.00'

Формат возврата средств в евро для этой ката должен быть следующим: '100,000.00€'

to_currencyэто строка со значениями 'USD','EUR', values_listэто список плавающих чисел

solution(to_currency,values)

#ПРИМЕРЫ:

solution('USD',[1394.0, 250.85, 721.3, 911.25, 1170.67])
= ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']

solution('EUR',[109.45, 640.31, 1310.99, 669.51, 415.54])
= ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€']

"""
import unittest
from typing import Any, Callable, List, Optional, Tuple
from operator import mul, truediv


def converter_course(to_cur: str, value: List[float], x: float = 1.1363636) -> Optional[List[str]]:
    data = {
        'USD': (mul, ('$', '')),
        'EUR': (truediv, ('', '€')),
    }
    if data.get(to_cur):
        func, (a, b) = data[to_cur]
        return [f'{a}{(func(n, x)):,.2f}{b}' for n in value]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(converter_course, (
        (('USD', [1.01, 83.29, 5.0, 23.23, 724.22]), ['$1.15', '$94.65', '$5.68', '$26.40', '$822.98']),
        (('USD', [1394.0, 250.85, 721.3, 911.25, 1170.67]), ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']),
        (('EUR', [109.45, 640.31, 1310.99, 669.51, 415.54]), ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€']),
        (('EUR', [589.29, 662.31, 1349.71, 117.93, 8.25]), ['518.58€', '582.83€', '1,187.74€', '103.78€', '7.26€']),
    ))
