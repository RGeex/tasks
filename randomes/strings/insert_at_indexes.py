"""
Дорогой Кодер,

Мы в [SomeLargeCompany] решили расширить функциональность нашего
онлайн-текстового редактора.

Мы написали новую функцию, которая принимает фразу, слово и массив индексов.
Мы хотим, чтобы эта функция возвращала фразу со словом, вставленным в каждый
из индексов, заданных массивом.

Однако наша текущая функция правильно выполняет только первую вставку, а все
последующие неуместны!

Пожалуйста, исправьте это для нас, и вас засыплют деньгами.

Искренне Ваш, [Некоторая крупная компания]

Примечание :

    индексы всегда находятся в диапазоне и передаются как отсортированный
    массив
    обратите внимание, что если массив индексов пуст, просто верните начальную
    фразу
"""


def insert_at_indexes(phrase: str, word: str, indexes: list[int]) -> str:
    """
    Вставляет в строку заданное слово по указанным индексам.
    """
    for i in indexes[::-1]: 
        phrase = phrase[:i] + word + phrase[i:]
    return phrase



def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("I like codewars! It makes me happy."," really",[1, 28]), 'I really like codewars! It makes me really happy.'),
        (('I really like codewars! It makes me really happy.',"'d",[1, 26]), "I'd really like codewars! It'd makes me really happy."),
        (("'I' write a wi said Phi", "ll", [3, 14, 24]), "'I'll write a will said Phill"),
    )
    for key, val in data:
        assert insert_at_indexes(*key) == val


if __name__ == '__main__':
    test()
