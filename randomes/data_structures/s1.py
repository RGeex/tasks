"""
Двусвязный список:

Дан текстовый файл. Создайте двусвязный список,
каждый элемент которого содержит количество
символов в соответствующей строке текста.
"""

from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    """Хранение данных о строках и кол-ве символов в них."""
    line: int
    length: int


@dataclass(slots=True)
class Node:
    """Объект списка."""
    data: Item
    prev: Item | None = None
    next: Item | None = None


class ListNew:
    """Двусвязный список"""

    def __init__(self) -> None:
        self.head = None
        self.lenght = 0

    def __len__(self) -> int:
        return self.lenght

    def push(self, data: Item) -> None:
        """Добавление элементов в список"""
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
        self.head = node
        self.lenght += 1

    def print_list(self) -> None:
        """Распечатать список"""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


def main() -> None:
    """Считывание файла и создание на его основе двусвязного списка"""
    lst = ListNew()
    filename = Path(__file__).parent / '5.txt'

    with open(filename, 'r', encoding='UTF-8') as file:
        for i, line in enumerate(file, 1):
            lst.push(Item(i, len(line.rstrip('\n'))))

    lst.print_list()


def test() -> None:
    """Тестирование работы алгоритмов."""
    n = 10
    lst = ListNew()
    assert len(lst) == 0

    for i in range(1, n + 1):
        lst.push(Item(i, i * i))

    assert len(lst) == n


if __name__ == '__main__':
    test()
