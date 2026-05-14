"""
Ваши коллеги следили за вами. Вместо того чтобы заниматься своей скучной основной работой,
вы использовали рабочие компьютеры, чтобы часами без конца заниматься программированием.

На командном совещании какой-то ужасный, отвратительный человек заявляет группе,
что вы не работаете. У вас проблемы. Вам нужно быстро оценить настроение в комнате,
чтобы решить, следует ли вам собрать свои вещи и уйти.

Дана данная модель объекта ( meetЕсли переменная содержит имена членов команды в качестве ключей и
их оценку удовлетворенности по 10-балльной шкале в качестве значения, вам необходимо оценить общую
оценку удовлетворенности группы. Если значение <= 5, верните «Убирайтесь отсюда!».
В противном случае верните «Отличная работа, чемпион!».

Рейтинг счастья будет рассчитываться как общее количество баллов, деленное на число людей в комнате.

Обратите внимание, что ваш начальник находится в комнате. bossИх результат вдвое превышает
номинальную стоимость (но это всё ещё всего один человек!).

"""
import unittest
from typing import Any, Callable, Tuple


def outed(meet: dict[str, int], boss: str) -> str:
    """
    Определяет что необходимо ответить коллегам.
    """
    return ['Nice Work Champ!', 'Get Out Now!'][(sum(meet.values()) + meet.get(boss, 0)) / len(meet) <= 5]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(outed, (
        (({'tim': 0, 'jim': 2, 'randy': 0, 'sandy': 7, 'andy': 0, 'katie': 5, 'laura': 1, 'saajid': 2, 'alex': 3, 'john': 2, 'mr': 0}, 'laura'), 'Get Out Now!'),
        (({'tim': 1, 'jim': 3, 'randy': 9, 'sandy': 6, 'andy': 7, 'katie': 6, 'laura': 9, 'saajid': 9, 'alex': 9, 'john': 9, 'mr': 8}, 'katie'), 'Nice Work Champ!'),
        (({'tim': 2, 'jim': 4, 'randy': 0, 'sandy': 5, 'andy': 8, 'katie': 6, 'laura': 2, 'saajid': 2, 'alex': 3, 'john': 2, 'mr': 8}, 'john'), 'Get Out Now!'),
    ))
