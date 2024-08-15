"""
Вам будет предоставлена ​​последовательность объектов (ассоциативные массивы в PHP),
представляющих данные о разработчиках, которые зарегистрировались для участия в
следующей конференции по программированию, которую вы организуете.

Ваша задача вернуть:

    true если все следующие континенты/географические зоны будут представлены
    хотя бы одним разработчиком: «Африка», «Америка», «Азия», «Европа», «Океания».
    false в противном случае.

Например, учитывая следующий входной массив:

list1 =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]

ваша функция должна вернуть true так как есть хотя бы один застройщик из
необходимых 5 географических зон.

Примечания:

    Названия входного массива и континентов всегда будут действительны и
    отформатированы, как в списке выше, например, «Африка» всегда будет
    начинаться с буквы «А» в верхнем регистре.
"""


def all_continents(lst: list[dict]) -> bool:
    """
    Проверяет наличие разработчиков со всех континентов.
    """
    return not set('Africa Americas Asia Europe Oceania'.split()) - {x['continent'] for x in lst}


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([
            { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
            { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
            { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
            { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
            { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
        ], True),
        ([
            { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' }
        ], False)
    )
    for key, val in data:
        assert all_continents(key) == val


if __name__ == '__main__':
    test()
