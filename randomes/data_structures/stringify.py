"""
Преобразовать связанный список в строку.
Связанные слова

вы также можете попробовать выполнить разбор связанного списка из строки . Хотя эта задача не является частью официальной серии, если она вам понравилась,
Предварительно загружено

Вам предварительно загружены класс, структура или производный тип данных. Node(в зависимости от языка), используемого для построения связанных списков в этом задании:

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

Предварительные требования

В этом задании предполагается, что вы уже знакомы с понятием связанного списка.
Если вы не знаете, что это такое, вы можете прочитать эту статью в Википедии .
В частности, в этом задании речь идёт об односвязных списках , где значение конкретного
узла хранится в его собственном счётчике. data/ $data/ Dataсвойство, ссылка на следующий
узел хранится в его next/ $next/ Next/ next_nodeсвойство, а завершающим элементом списка
является null/ NULL/ None/ nil/ nullptr/ null().
Задача

Создайте функцию stringifyкоторый принимает аргумент list/ $listи возвращает строковое
представление списка. Строковое представление списка начинается со значения текущего
элемента. Node, указанный его data/ $data/ Dataсвойство, за которым следует пробел,
стрелка и еще один пробел ( " -> "), за которым следует остальная часть списка.
Конец строкового представления списка всегда должен заканчиваться на
null/ NULL/ None/ nil/ nullptr/ null()(Все буквы заглавные или строчные,
в зависимости от языка, на котором вы выполняете это задание).
Например, если дан следующий список:

Node(1, Node(2, Node(3)))

... в строковом представлении это будет выглядеть так:

"1 -> 2 -> 3 -> None"

И учитывая следующий связанный список:

Node(0, Node(1, Node(4, Node(9, Node(16)))))

... в строковом представлении это будет выглядеть так:

"0 -> 1 -> 4 -> 9 -> 16 -> None"

Обратите внимание, что null/ NULL/ None/ nil/ nullptr/ null()
Сам по себе он также считается допустимым связанным списком. В этом случае его
строковое представление будет просто следующим:
"null"/ "NULL"/ "None"/ "nil"/ "nullptr"/ @"NULL"/ "null()"(опять же, в зависимости от языка).

Для простоты этой ката можно предположить, что любой NodeВ этом задании Kata могут содержаться
только неотрицательные целые значения. Например, вы не встретите...
Node чей data/ $data/ Dataсобственность "Hello World".
"""
import unittest
from typing import Any, Callable, Tuple


class Node():
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


def stringify_1(node: Node | None) -> str:
    """
    Создает из связного списка строку.
    """
    return f'{node.data} -> {stringify_1(node.next)}' if node else 'None'


def stringify_2(node: Node | None) -> str:
    """
    Создает из связного списка строку.
    """
    return str(node and f'{node.data} -> ') + (stringify_2(node.next) if node else '')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(stringify_1, (
        (Node(0, Node(1, Node(2, Node(3)))), '0 -> 1 -> 2 -> 3 -> None'),
        (None, 'None'),
        (Node(0, Node(1, Node(4, Node(9, Node(16))))), '0 -> 1 -> 4 -> 9 -> 16 -> None'),
    ))
    test(stringify_2, (
        (Node(0, Node(1, Node(2, Node(3)))), '0 -> 1 -> 2 -> 3 -> None'),
        (None, 'None'),
        (Node(0, Node(1, Node(4, Node(9, Node(16))))), '0 -> 1 -> 4 -> 9 -> 16 -> None'),
    ))
