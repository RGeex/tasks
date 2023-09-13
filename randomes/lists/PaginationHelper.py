"""
В этом упражнении вы укрепите свое мастерство паж-фу. Вы завершите
работу над классом PaginationHelper, который представляет собой
служебный класс, полезный для запроса информации о подкачке,
связанной с массивом.

Класс предназначен для приема массива значений и целого числа,
указывающего, сколько элементов будет разрешено на каждой странице.
Типы значений, содержащихся в коллекции/массиве, не имеют значения.
"""


class PaginationHelper:
    """
    Вспомогательный класс, для получения детальной информации о
    получаемом списке данных.
    """

    def __init__(self, collection, items_per_page):
        self.coll = collection
        self.item = items_per_page
        self.a, self.b = divmod(self.item_count(), self.item)

    def item_count(self):
        """
        Длина списка.
        """
        return len(self.coll)

    def page_count(self):
        """
        Кол-во страниц для размещения всех данных.
        """
        return self.a + bool(self.b)

    def page_item_count(self, page_index):
        """
        Кол-во элементов на указанной странице.
        """
        if page_index in range(self.page_count()):
            return [self.b, self.item][page_index < self.a]
        return -1

    def page_index(self, item_index):
        """
        Номер страницы по индексу элемента.
        """
        if item_index in range(self.item_count()):
            return item_index // self.item
        return -1


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    collection = ['a', 'b', 'c', 'd', 'e', 'f']
    helper = PaginationHelper(collection, 4)

    assert helper.page_count() == 2
    assert helper.item_count() == 6

    assert helper.page_item_count(0) == 4
    assert helper.page_item_count(1) == 2
    assert helper.page_item_count(2) == -1

    assert helper.page_index(5) == 1
    assert helper.page_index(2) == 0
    assert helper.page_index(20) == -1
    assert helper.page_index(-10) == -1

    empty = PaginationHelper([], 10)
    assert empty.item_count() == 0
    assert empty.page_count() == 0
    assert empty.page_index(0) == -1
    assert empty.page_index(1) == -1
    assert empty.page_index(-1) == -1
    assert empty.page_item_count(0) == -1
    assert empty.page_item_count(1) == -1
    assert empty.page_item_count(-1) == -1


if __name__ == '__main__':
    test()
