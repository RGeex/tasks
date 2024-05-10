"""
Вам будет предоставлена ​​последовательность объектов, представляющих данные о
разработчиках, которые зарегистрировались для участия в следующей конференции
по программированию, которую вы организуете.

Ваша задача — вернуть последовательность, включающую самого старшего
разработчика. В случае равенства включите всех старших разработчиков одного
возраста, перечисленных в том же порядке, в котором они указаны в исходном
входном массиве.

Например, учитывая следующий входной массив:

list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]

ваша функция должна возвращать следующий массив:

[
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]

Примечания:

    Входной массив всегда будет действительным и отформатированным, как в
    примере выше, и никогда не будет пустым. 
"""



def find_senior(lst: list[dict]) -> list[dict]:
    """
    Поиск всех сотрудников с максимальным возрастом.
    """
    age, res = 0, []
    for x in lst:
        if age == x['age']:
            res.append(x)
        if age < x['age']:
            res, age = [x], x['age']
    return res


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
            { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
            { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
        ],
        [
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
        ]),
        ([
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
            { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
            { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
        ],
        [
            { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
        ]),
        ([
            { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
            { 'firstName': 'Fatima', 'lastName': 'K.', 'country': 'Saudi Arabia', 'continent': 'Asia', 'age': 21, 'language': 'Clojure' },
            { 'firstName': 'Mark', 'lastName': 'G.', 'country': 'Scotland', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
            { 'firstName': 'Nikola', 'lastName': 'H.', 'country': 'Serbia', 'continent': 'Europe', 'age': 29, 'language': 'Python' },
            { 'firstName': 'Jakub', 'lastName': 'I.', 'country': 'Slovakia', 'continent': 'Europe', 'age': 28, 'language': 'Java' },
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 89, 'language': 'JavaScript' },
            { 'firstName': 'Luka', 'lastName': 'J.', 'country': 'Slovenia', 'continent': 'Europe', 'age': 29, 'language': 'Clojure' },
            { 'firstName': 'Mariam', 'lastName': 'B.', 'country': 'Egypt', 'continent': 'Africa', 'age': 89, 'language': 'Python' },
        ],
        [
            { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 89, 'language': 'JavaScript' },
            { 'firstName': 'Mariam', 'lastName': 'B.', 'country': 'Egypt', 'continent': 'Africa', 'age': 89, 'language': 'Python' },
        ]),
    )
    for key, val in data:
        assert find_senior(key) == val


if __name__ == '__main__':
    test()
