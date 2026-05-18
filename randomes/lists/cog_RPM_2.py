"""
Ключевые слова задания

Вам предоставлен список шестеренок зубчатой ​​передачи и указатель. nдля nthвинтик в списке.

Каждый элемент представляет собой количество зубьев данной шестерни.

например [100, 50, 25] означает

    Первая шестерня имеет 100 зубьев.
    Вторая шестерня имеет 50 зубьев.
    Третья шестерня имеет 25 зубьев.

Если nthЗубчатое колесо вращается по часовой стрелке со скоростью 1 об/мин. Какова частота вращения зубчатых колес на каждом конце зубчатой ​​передачи?

Примечания

    Нет двух шестеренок с одним и тем же валом.
    Возвращает массив, два элемента которого представляют собой обороты в минуту первой и последней шестерен соответственно.
    Для вращения против часовой стрелки используйте отрицательные числа.
    для удобства nнулевая отсчетная база

"""
import unittest
from typing import Any, Callable, List, Tuple


def cog_RPM(cogs: List[int], n: int) -> List[float]:
    """
    Определяет частоту вращения колес.
    """
    return [cogs[n]/cogs[0] * (-1)**n, cogs[n]/cogs[-1] * (-1)**(len(cogs)-n-1)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(cog_RPM, (
        (([100, 50, 25], 1), [-1/2, -2]),
    ))
