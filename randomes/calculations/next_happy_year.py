"""
Сценарий
Ты прощаешься со своим лучшим другом . Увидимся в следующем счастливом году !

Счастливый год — это год, состоящий только из отдельных цифр , например, 2018 .

Задача
Найдите год, который станет для вас следующим счастливым годом , или год, в котором вы увидите
своего лучшего друга ближе всего к этому времени.!alt!alt

Примечания
Конечно, в этом году всегда позитивно .
Не бойтесь , ответ гарантированно существует .
Необязательно , чтобы годом, передаваемым для функции, был «Счастливый год» .
Введите год в пределах диапазона (1000 ≤ y ≤ 9000)
Примеры ввода и вывода:
nextHappyYear (7712) ==> return (7801)
Объяснение :
Ближайший год, содержащий только уникальные цифры, — 7801 .

nextHappyYear (8989) ==> return (9012)
Объяснение :
Ближайший год, состоящий только из уникальных цифр, — 9012 .

nextHappyYear (1001) ==> return (1023)
Объяснение :
Ближайший год, состоящий только из уникальных цифр, — 1023 .
"""
import unittest
from typing import Any, Callable, Tuple


def next_happy_year(year: int) -> int:
    """
    Вычисляет следующий год с уникальными цифрами.
    """
    while len(set(str(year := year + 1))) != 4:
        pass
    return year


def next_happy_year_2(year: int) -> int:
    """
    Вычисляет следующий год с уникальными цифрами.
    """
    return year if len(set(str(year := year + 1))) == 4 else next_happy_year_2(year)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(next_happy_year, (
        (1001, 1023),
        (1123, 1203),
        (2001, 2013),
        (2334, 2340),
        (3331, 3401),
        (1987, 2013),
        (5555, 5601),
        (7712, 7801),
        (8088, 8091),
        (8999, 9012),
    ))
    test(next_happy_year_2, (
        (1001, 1023),
        (1123, 1203),
        (2001, 2013),
        (2334, 2340),
        (3331, 3401),
        (1987, 2013),
        (5555, 5601),
        (7712, 7801),
        (8088, 8091),
        (8999, 9012),
    ))
