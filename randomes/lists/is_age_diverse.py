"""
Вам будет предоставлен массив объектов (ассоциативные массивы в PHP),
представляющих данные о разработчиках, которые зарегистрировались
для участия в следующей конференции по программированию, которую вы
организуете.

Ваша задача вернуть:

    true если зарегистрировались разработчики из всех следующих возрастных
    групп: подростки, двадцатилетние, тридцатые, сороковые, пятидесятые,
    шестидесятые, семидесятые, восьмидесятые, девяностые, столетние
    (молодые не менее 100 лет).
    false в противном случае.

Например, учитывая следующий входной массив:

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
  { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
  { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
  { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
  { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
]

ваша функция должна вернуть true поскольку в каждой возрастной группе есть
хотя бы один разработчик.

Примечания:

    Входной массив всегда будет действительным и отформатирован,
    как в примере выше.
    Возраст представлен числом, которое может быть любым
    положительным целым числом до 199.
"""


def is_age_diverse(lst: list[dict]) -> bool:
    """
    Проверяет, принадлежат ли все участники конференции
    ко всем возрастным группам.
    """
    return len({x['age'] // 10 for x in lst if 0 < x['age'] // 10 < 10}) == 9


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([
            { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
            { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
            { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
            { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
            { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
            { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
            { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
            { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
            { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
        ], True),
        ([
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'Ruby' },
            { 'firstName': 'Amar', 'lastName': 'V.', 'country': 'Bosnia and Herzegovina', 'continent': 'Europe', 'age': 32, 'language': 'Ruby' },
        ], False),
        ([
            { 'firstName': 'Sofia', 'lastName': 'P.', 'country': 'Italy', 'continent': 'Europe', 'age': 41, 'language': 'Clojure' },
            { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
            { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Python' },
            { 'firstName': 'Rimas', 'lastName': 'C.', 'country': 'Jordan', 'continent': 'Asia', 'age': 44, 'language': 'Java' }
        ], False),
    )
    for key, val in data:
        assert is_age_diverse(key) == val


if __name__ == '__main__':
    test()
