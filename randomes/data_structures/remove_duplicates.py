"""
Напишите код для удаления дубликатов из несортированного связного списка.
"""

from dataclasses import dataclass


Item = int


@dataclass(slots=True)
class Node:
    """Нода списка."""
    data: Item
    next: Item | None = None

    def __str__(self) -> str:
        return f'{self.data}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.data})'

    def __hash__(self) -> int:
        return hash(self.data)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.data == other.data
        return NotImplemented


class ListNew:
    """Односвязный список."""

    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.lenght = 0

    def __str__(self) -> str:
        return f'{self.lst_from_obj}'

    def __len__(self) -> int:
        return self.lenght

    def __hash__(self) -> int:
        return hash(self.lst_from_obj)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ListNew):
            return self.lst_from_obj == other.lst_from_obj

        if isinstance(other, list):
            return self.lst_from_obj == other

        return NotImplemented

    @property
    def lst_from_obj(self) -> list:
        """Создает обычный список из текущего объекта."""
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next

        return result

    def append(self, data: Item) -> None:
        """Добавляет элемент в конец списка."""

        node = Node(data)

        if self.head is None:
            self.head = node

        if self.tail is not None:
            self.tail.next = node

        self.tail = node
        self.lenght += 1

    def get_hash(self) -> dict:
        """Хеширование элементов списка и поиск одинаковых значений."""

        node = self.head
        data = {}
        while node:
            data[node] = data.get(node, 0) + 1
            node = node.next

        return data

    def remove_duplicates(self) -> None:
        """Удаляет дубликаты из списка."""
        if not self.lenght:
            return

        data = self.get_hash()
        node = self.head
        prev = node
        while node:

            if data.get(node, 0) > 1:
                if self.head == node:
                    self.head = node.next
                else:
                    prev.next = node.next

                self.lenght -= 1
                data[node] -= 1

            prev, node = node, node.next


def add_to_lst(items: list, lst: ListNew | None = None) -> ListNew:
    """Добавляет элементы к односвязному списку, если список не передан
    в качестве аргумента, создается новый список."""
    lst = lst or ListNew()

    for item in items:
        lst.append(item)

    return lst


def test() -> None:
    """Тестирование работы алгоритмов."""
    lst1 = [1, 2, 3, 9, 2, 8, 7, 2, 1, 3]
    lst2 = [9, 8, 7, 2, 1, 3]
    obj1 = add_to_lst(lst1)

    assert obj1 == lst1
    obj1.remove_duplicates()
    assert obj1 == lst2


if __name__ == '__main__':
    test()
