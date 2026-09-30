"""
Вам предоставлен список записей журнала из системы. Каждая запись журнала имеет следующий формат:
"LEVEL message", где LEVEL — один из значений INFO, WARNING, ERROR.

Ваша задача — сжать последовательные идентичные записи в журнале, добавив счетчик повторений.

Правила:
Сжимать следует только последовательные идентичные записи.
Сравнение должно учитывать регистр символов.
Исходное сообщение журнала необходимо сохранить.
Единственное обнаруженное событие должно остаться без изменений.
Повторяющиеся записи следует заменить записью, за которой следует " (xN)", где N— количество повторений.
Порядок записей в логах должен оставаться неизменным.
Если входной список пуст, вернуть пустой список.
Примеры
#### Input
[
"ERROR Disk failure",
"ERROR Disk failure",
"ERROR Disk failure",
"INFO User login"
]

#### Output
[
"ERROR Disk failure (x3)",
"INFO User login"
]
Пояснение: Три последовательные "ERROR Disk failure"записи объединены в одну.

#### Input
[
"INFO Connected",
"WARNING Low battery",
"INFO Connected"
]

#### Output
[
"INFO Connected",
"WARNING Low battery",
"INFO Connected"
]
Пояснение: Сжимаются только последовательные идентичные записи в логах. Две INFOзаписи не расположены рядом, поэтому они остаются раздельными.
"""
import unittest
from typing import Any, Callable, List, Tuple
from itertools import groupby


def smart_log_formatter(logs: List[str]) -> List[str]:
    """
    Анализирует логи и группирпует значения идущие подряд.
    """
    return [a + (f" (x{x})" if (x := len(list(b))) > 1 else "") for a, b in groupby(logs)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(smart_log_formatter, (
        ([
            "ERROR Disk failure",
            "ERROR Disk failure",
            "ERROR Disk failure",
            "INFO User login"
        ],
        [
            "ERROR Disk failure (x3)",
            "INFO User login"
        ]),
        ([
            "INFO Connected",
            "WARNING Low battery",
            "INFO Connected"
        ],
        [
            "INFO Connected",
            "WARNING Low battery",
            "INFO Connected"
        ]),
        ([
            "INFO Start",
            "INFO Start"
        ],
        [
            "INFO Start (x2)"
        ]),
    ))
