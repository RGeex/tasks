"""
История

Вы и группа друзей подрабатываете во время школьных каникул,
перекрашивая цифры на почтовых ящиках за небольшую плату.

Поскольку вас в группе 10 человек, каждый участник сосредотачивается на рисовании только одной
цифры! Например, кто-то будет рисовать только одну цифру. 1кто-то другой нарисует только это.
2и так далее...

Но в конечном итоге понимаешь, что не все проделали одинаковый объем работы.

Чтобы избежать ссор, нужно справедливо распределить деньги. Вот тут-то и пригодится эта ката.
Ключевые слова задания

Учитывая start и endДля отображения цифр в почтовом ящике напишите метод, который возвращает
частоту появления всех 10 отображаемых цифр.
Пример

Для start= 125, и end= 132

Почтовые ящики

    125 = 1, 2, 5
    126 = 1, 2, 6
    127 = 1, 2, 7
    128 = 1, 2, 8
    129 = 1, 2, 9
    130 = 1, 3, 0
    131 = 1, 3, 1
    132 = 1, 3, 2

Частота встречаемости цифр следующая:

    0раскрашено 1 раз
    1рисуется 9 раз
    2рисуется 6 раз
    и т. д...

и, следовательно, метод вернет [1,9,6,3,0,1,1,1,1,1]
Примечания

    0 < start<= end
"""
import unittest
from typing import Any, Callable, List, Tuple


def paint_letterboxes(start: int, finish: int) -> List[int]:
    """
    Определяет кол-во одинаковых цифр в числах диапазона.
    """
    return [''.join(map(str, range(start, finish + 1))).count(str(i)) for i in range(10)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(paint_letterboxes, (
        ((125, 132), [1, 9, 6, 3, 0, 1, 1, 1, 1, 1]),
    ))
