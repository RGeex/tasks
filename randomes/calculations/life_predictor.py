"""
Почти каждый знает свой день рождения. Однако к моменту рождения
мы уже примерно десять месяцев живем. Лишь немногие знают точную дату,
когда по-настоящему началась наша жизнь. Поэтому давайте создадим своего
рода предсказатель жизни, который поможет нам определить этот особенный момент.

Период беременности составляет около 280 дней с погрешностью в одну-две недели.
Здесь мы просто проигнорируем эту погрешность и будем использовать 280 дней для прогноза.

В этом задании используется григорианский календарь . Високосный год требует особого внимания.
Поскольку григорианский календарь появился только в октябре 1582 года, все тестовые случаи будут
относиться к датам после этого времени.

Входными данными является дата рождения в формате "ГГГГ-ММ-ДД".

Дата вывода также имеет тот же формат.

  life_predictor("2000-09-18")  #result is "1999-12-13"

Надеюсь, вам понравится ката, и вы узнаете несколько интересных фактов!
"""
import unittest
from typing import Any, Callable, Tuple
from datetime import datetime, timedelta


def life_predictor(date: str) -> str:
    """
    Определяет дату создания новой жизни.
    """
    return str((datetime.strptime(date, '%Y-%m-%d') - timedelta(days=280)).date())




def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(life_predictor, (
        ("2000-09-18", "1999-12-13"),
    ))
