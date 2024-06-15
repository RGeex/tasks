"""
Вам будет предоставлен массив объектов, представляющих данные о разработчиках,
которые зарегистрировались для участия в следующей конференции по
программированию, которую вы организуете.

Учитывая следующий входной массив:

var list1 = [
  { firstName: 'Aba', lastName: 'N.', country: 'Ghana', continent: 'Africa', age: 21, language: 'Python' },
  { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
];

напишите функцию, которая при выполнении как findOddNames(list1) возвращает
только разработчиков, где, если вы добавите ASCII-представление всех символов
в их имена, результатом будет нечетное число :

[
  { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
]

Пояснение к вышесказанному:

    Сумма кодов букв ASCII в 'Aba' является: 65 + 98 + 97 = 260 что является
    четным числом
    Сумма кодов букв ASCII в 'Abb' является: 65 + 98 + 98 = 261 что является
    нечетным числом

Примечания:

    Сохраните порядок исходного списка.
    Вернуть пустой массив [] если нет разработчика с "нечетным" именем.
    Входной массив и имена всегда будут действительны и отформатированы, как в
    примере выше.
"""


def find_odd_names(lst: list[dict]) -> list[dict]:
    """
    Поиск в списке разработчиков, сумма чьих имен в ASCI нечетная.
    """ 
    return [x for x in lst if sum(map(ord, x['firstName'])) % 2]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([
            { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
            { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' },
        ],
        [
            { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' },
        ]),
        ([
            { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
        ],
        []),
    )
    for key, val in data:
        assert find_odd_names(key) == val


if __name__ == '__main__':
    test()
