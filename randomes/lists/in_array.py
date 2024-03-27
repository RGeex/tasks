"""
Учитывая два массива строк a1и a2вернуть отсортированный массив rв лексикографическом порядке строк
a1 которые являются подстроками строк a2.
Пример 1:

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

возвращает ["arp", "live", "strong"]
Пример 2:

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

возвращает []
Примечания:

    Массивы записываются в «общих» обозначениях. См. «Ваши тестовые примеры» для примеров на
    вашем языке.
    В Shell bash a1и a2являются струнами. Возврат представляет собой строку, в которой слова
    разделены запятыми.
    Внимание: на некоторых языках rдолжно быть без дубликатов.
"""

def in_array(arr1, arr2):
    return not (r := set()) and sorted(next((0 for w2 in arr2 if r.update(w1 for w1 in arr1 if w1 in w2)), r))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]), ['arp', 'live', 'strong']),
        ((["arp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]),['arp']),
    )
    for key, val in data:
        assert in_array(*key) == val


if __name__ == '__main__':
    test()
