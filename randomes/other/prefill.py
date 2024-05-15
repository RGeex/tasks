"""
Создайте функцию prefillкоторый возвращает массив nэлементы, которые все имеют
одинаковое значение v. Посмотрите, сможете ли вы сделать это без использования
цикла.

Вам необходимо подтвердить ввод:

    v может быть чем угодно (примитивным или другим)
    если v опущен, заполните массив undefined
    если n равно 0, вернуть пустой массив
    если n является чем-либо иным, чем целочисленная строка или строка в
    целочисленном формате (например, '123') то есть >=0, бросить TypeError

Когда бросаешь TypeError, сообщение должно быть n is invalid, где вы замените n
для фактического значения, переданного в функцию.

Примеры кода

    prefill(3,1) --> [1,1,1]
    
    prefill(2,"abc") --> ['abc','abc']
    
    prefill("1", 1) --> [1]
    
    prefill(3, prefill(2,'2d'))
      --> [['2d','2d'],['2d','2d'],['2d','2d']]
      
    prefill("xyz", 1)
      --> throws TypeError with message "xyz is invalid"
"""


def prefill(n: int | str, v='undefined') -> list:
    """
    Проверяет тип входящих данных и создает список значений в
    заданном кол-ве.
    """
    if isinstance(n, int) or isinstance(n, str) and n.isdigit():
        return int(n) * [v]
    raise TypeError(f'{n} is invalid')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((3,1), [1,1,1]),
        ((2,'abc'), ['abc','abc']),
        (('1',1), [1]),
        ((3, ['2d','2d']), [['2d','2d'],['2d','2d'],['2d','2d']]),
    )
    for key, val in data:
        assert prefill(*key) == val

    try:
        prefill('xyz', 1)
    except TypeError as err:
        assert str(err) == "xyz is invalid"


if __name__ == '__main__':
    test()
