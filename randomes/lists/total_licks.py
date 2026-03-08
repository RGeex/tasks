"""
Сколько раз нужно лизнуть леденец Tootsie Pop, чтобы добраться до его начинки?

Группа студентов-инженеров из Университета Пердью сообщила, что их машина для облизывания,
смоделированная по образцу человеческого языка, в среднем совершила 364 облизывания,
чтобы добраться до центра леденца Tootsie Pop. Двадцать добровольцев из этой группы
приняли участие в испытании — без помощи техники — и в среднем совершили по 252 облизывания до
центра.

Ваша задача, если вы решите её принять, — написать функцию, которая будет возвращать количество
лизков, необходимых для того, чтобы добраться до центра конфеты Tootsie Pop, при условии знания
некоторых переменных окружения.

Всем известно, что в холодную погоду сложнее облизать леденец Tootsie Pop, но на солнце это сделать
проще. Для каждого испытания вам будет предоставлен объект, определяющий условия окружающей среды,
в паре с которым будет указано значение, увеличивающее или уменьшающее количество облизываний.
Все условия окружающей среды относятся к одному и тому же испытанию.

Предположим, что для того, чтобы добраться до сердцевины леденца Tootsie Pop, обычно требуется
252 облизывания. Верните новое общее количество облизываний, а также условие, которое оказалось
наиболее сложным (приведшим к наибольшему количеству дополнительных облизываний) в этом эксперименте.

Пример:

totalLicks({ "freezing temps": 10, "clear skies": -2 });

Должен вернуться:

"It took 260 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was freezing temps."

Другие случаи: Если нет сложных заданий, предложение с самым сложным заданием следует опустить.
Если заданий несколько, и каждое из них имеет наибольшую сложность, то самым сложным будет первое
представленное задание. Если переменная окружения присутствует, она будет либо положительным,
либо отрицательным целым числом. Проверять её не нужно.
"""
import unittest
from typing import Any, Callable, Dict, Tuple


def total_licks(env: Dict) -> str:
    """
    Определяет кол-во лизаний необходимых для того что бы добраться до центра конфеты.
    """
    num, (key_t, val_t) = 252, ('', 0)
    for key, val in env.items():
        num += val
        key_t, val_t = (key, val) if val > val_t else (key_t, val_t)
    tmp = f' The toughest challenge was {key_t}.' if val_t > 0 else ''
    return f'It took {num} licks to get to the tootsie roll center of a tootsie pop.{tmp}'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(total_licks, (
        ({ "freezing temps": 10, "clear skies": -2 },
        "It took 260 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was freezing temps."),

        ({ "happiness": -5, "clear skies": -2 },
        "It took 245 licks to get to the tootsie roll center of a tootsie pop."),
        
        ({},
        "It took 252 licks to get to the tootsie roll center of a tootsie pop."),

        ({"dragons": 100, "evil wizards": 110, "trolls": 50},
        "It took 512 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was evil wizards."),

        ({"white magic": -250},
        "It took 2 licks to get to the tootsie roll center of a tootsie pop."),
    ))
