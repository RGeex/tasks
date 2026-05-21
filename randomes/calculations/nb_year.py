"""
В небольшом городе население составляет p0 = 1000в начале года.
Население регулярно увеличивается на 2 percentв год и, кроме того 50Каждый год в город
приезжают новые жители. Сколько лет потребуется городу, чтобы его население выросло?
больше или равно p = 1200жителей?

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.

Более общие заданные параметры:

p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

функция nb_yearдолжен вернуться nколичество полных лет, необходимых для того,
чтобы численность населения превысила или сравнялась с p.

aug — целое число, percent — положительное или нулевое число с плавающей запятой,
p0 и p — положительные целые числа (> 0).

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10

Примечание:

    Не забудьте преобразовать параметр percent в процентное значение в теле вашей функции: если параметр percent равен 2, его необходимо преобразовать в 0,02.

    Долей населения не существует. В конце каждого года численность населения представляет собой целое число: 252.8люди округляют в меньшую сторону до 252лиц.

"""
import unittest
from typing import Any, Callable, Tuple


def nb_year(p0: int, percent: int | float, aug: int, p: int) -> int:
    """
    Расчитывает кол-во лет необходимых для поднятия населения до заданного значения.
    """
    n = 1
    while p > (p0 := int(p0 + p0 * (percent / 100) + aug)):
        n += 1
    return n


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(nb_year, (
        ((1500, 5, 100, 5000), 15),
        ((1500000, 2.5, 10000, 2000000), 10),
        ((1500000, 0.25, 1000, 2000000), 94),
    ))
