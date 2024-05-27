"""
Введение

Игровой автомат (американский английский), неофициально фруктовый автомат
(британский английский), мопс (шотландский английский сленг), игровые
автоматы (канадский и американский английский), покерный автомат
(или игровые автоматы на сленге) (австралийский английский и
новозеландский английский) или просто игровой автомат
(Американский английский) — игровой автомат для казино с тремя или более
барабанами, которые вращаются при нажатии кнопки.   Игровые автоматы
также известны как однорукие бандиты, потому что изначально ими
управлял один рычаг на боковой стороне автомата, а не кнопка на
передней панели, а также из-за их способности оставлять игрока в долгах
и нищете.   Многие современные машины помимо кнопки до сих пор оснащены
устаревшим рычагом.   (Источник  Википедия)


Задача

Вам будут предоставлены три барабана с разными изображениями и сообщено, на
каком индексе барабаны останавливаются.  На основе этой информации ваша
задача — вернуть счет полученных барабанов.


Правила

1. Всегда есть именно три  катушки

2. На каждом барабане есть 10  разные предметы.

3. Три барабанных входа могут быть разными.

4. Массив спинов представляет собой индекс  где заканчиваются барабаны.

5. Три спиновых входа могут быть разными.

6. Три одинаковых стоят больше, чем два одинаковых

7. Два одинаковых плюс один "Дикий"  это двойной результат.

8. Ни один подходящий товар не возвращается. 0.
"""


from collections import Counter


def fruit(reels: list[list[str]], spins: list[int]) -> int:
    """
    Определяет результат автомата, после выпадения значений.
    """
    res, comb = 0, dict(zip('Jack Queen King Bar Cherry Seven Shell Bell Star Wild'.split(), range(1, 11)))
    for i, (k, v) in enumerate(sorted(Counter([x[n] for x, n in zip(reels, spins)]).items(), key=lambda x: -x[1])):
        res = comb[k] * [1, 10][v == 3] if not i and 1 < v else [res, res * 2][k == 'Wild']
    return res


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([
            ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"],
            ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"],
            ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"],
        ], [0, 0, 0]), 100),
        (([
            ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"],
            ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"],
            ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"],
        ], [5, 4, 3]), 0),
        (([
            ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"],
            ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"],
            ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"],
        ], [0, 0, 1]), 3),
        (([
            ["King", "Jack", "Wild", "Bell", "Star", "Seven", "Queen", "Cherry", "Shell", "Bar"],
            ["Star", "Bar", "Jack", "Seven", "Queen", "Wild", "King", "Bell", "Cherry", "Shell"],
            ["King", "Bell", "Jack", "Shell", "Star", "Cherry", "Queen", "Bar", "Wild", "Seven"],
        ], [0, 5, 0]), 6),
    )
    for key, val in data:
        assert fruit(*key) == val


if __name__ == '__main__':
    test()
