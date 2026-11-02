"""
Алгоритмы планирования дисковых операций — это методы, используемые операционными системами для
определения порядка обработки запросов на чтение и запись жестким диском (HDD). Их основная цель
— сокращение времени поиска, то есть времени, необходимого головке диска для перемещения между
дорожками, что повышает общую производительность и пропускную способность системы.

Алгоритм планирования дисковых операций SSTF
Алгоритм SSTF (Shortest Hesk Time First) обрабатывает запросы ввода-вывода, наиболее близкие к
текущему положению головки диска. Всегда выбирая запрос с наименьшим расстоянием поиска, он
уменьшает общее перемещение головки и, как правило, обеспечивает лучшую производительность,
чем другие методы. Однако запросы, находящиеся далеко от текущего положения головки, могут
испытывать длительное время ожидания, что потенциально может привести к «голоданию» (starving).

Ваша задача — реализовать этот алгоритм. Функция будет принимать на вход два параметра: a request
queue— список целых чисел, представляющих адреса на диске, к которым необходимо обратиться для
выполнения ожидающих запросов ввода-вывода, и b — initial head positionцелое число, представляющее
начальную позицию головки диска. На каждом шаге функция должна выбирать и обрабатывать ожидающий
запрос, который находится ближе всего к текущей позиции головки. Этот процесс продолжается до тех
пор, пока не будут обработаны все запросы. Если два или более ожидающих запроса находятся на
одинаковом расстоянии от текущей позиции головки, алгоритм должен обработать тот запрос, который
появляется первым в очереди запросов.

Ожидаемый результат — это общее количество перемещений головки очереди, представленное целым числом,
соответствующим сумме всех перемещений головки, необходимых для обработки запросов в очереди.

Пример:
Данный:

ОЧЕРЕДЬ ЗАПРОСОВ = [98, 183, 37, 122, 14, 124, 65, 67],
ИСХОДНОЕ ПОЛОЖЕНИЕ ГОЛОВЫ = 53,
The head moves from 53 to 65 -> +12 head movement;
The head moves from 65 to 67 -> +2 head movement;
The head moves from 67 to 37 -> +30 head movement;
The head moves from 37 to 14 -> +23 head movement;
The head moves from 14 to 98 -> +84 head movement;
The head moves from 98 to 122 -> +24 head movement;
The head moves from 122 to 124 -> +2 head movement;
The head moves from 124 to 183 -> +59 head movement;
The total head movement is 236.
"""
import unittest
from typing import Any, Callable, List, Tuple


def sstf(request_queue: List[int], initial_head_position: int) -> int:
    """
    Определяет кол-во шагов головки.
    """
    result = 0
    request_queue_copy = request_queue.copy()
    for _ in request_queue:
        x = min(request_queue_copy, key=lambda x: abs(x - initial_head_position))
        result += abs(x - initial_head_position)
        request_queue_copy.remove(x)
        initial_head_position = x
    return result


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sstf, (
        (([], 12), 0),
        (([98, 183, 37, 122, 14, 124, 65, 67], 53), 236),
        (([33, 25, 109, 201, 15, 22], 83), 306),
        (([110, 3, 15, 90, 33, 12, 16], 100), 117),
        (([23, 50, 97, 11, 102, 1], 60), 160),
        (([40, 60, 70], 50), 40),
    ))
