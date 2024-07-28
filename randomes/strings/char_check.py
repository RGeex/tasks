"""
Кара претендует на несколько разных вакансий. В онлайн-заявках ее просят
ответить в пределах определенного количества символов. Каре необходимо
проверить, соответствуют ли ее ответы ограниченному количеству символов.

Досадно то, что некоторые формы приложений считают пробелы за символы,
а некоторые нет.

Ваша задача:

Напишите Кара функцию charCheck() с аргументами:

    "text": строка, содержащая ответ Кары на вопрос.
    "max": число, равное максимальному количеству символов, разрешенному
    в ответе.
    "spaces": логическое значение, которое True если в число символов
    включены пробелы и False если они не

Функция charCheck() должен вернуть массив: [True, "Answer"] , где "Answer"
равно исходному тексту, если ответ Кары достаточно короткий.

Если ее ответ "text" слишком длинный, верните массив: [False, "Answer"].
Второй элемент должен быть оригинальным "text" строка усекается до предельной
длины.

Когда "spaces" аргумент это False, вам следует удалить пробелы из "Answer".

Например:

    charCheck("Cara Hertz", 10, True) должен вернуться [ True, "Cara Hertz" ]
    charCheck("Cara Hertz", 9, False) должен вернуться [ True, "CaraHertz" ]
    charCheck("Cara Hertz", 5, True) должен вернуться [ False, "Cara " ]
    charCheck("Cara Hertz", 5, False) должен вернуться [ False, "CaraH" ]
"""


def char_check(text: str, mx: int, spaces: bool) -> list[bool, str]:
    """
    Убирает из строки пробелы, если "spaces == True", подсчитывет в полученной строке
    кол-во символов и сравнивает с заданным, выводит допустима ли строка по символам,
    а так же строку в пределах заданного кол-ва символов.
    """
    return [len(x := text.replace(' ', ['', ' '][spaces])) <= mx, x[:mx]]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            ("I am applying for the role of Base Manager on Titan.", 60, True),
            [True, "I am applying for the role of Base Manager on Titan."]
        ),
        (
            ("I am looking to relocate to the vicinity of Saturn for family reasons.", 70, True),
            [True, "I am looking to relocate to the vicinity of Saturn for family reasons."]
        ),
        (
            ("As Deputy Base Manager on Phobos for five Martian years, I have significant relevant experience.", 90, False),
            [True, "AsDeputyBaseManageronPhobosforfiveMartianyears,Ihavesignificantrelevantexperience."]
        ),
        (
            ("A challenging career moment came with the rapid depletion of water supplies on Phobos.", 80, False),
            [True,"AchallengingcareermomentcamewiththerapiddepletionofwatersuppliesonPhobos."]
        ),
        (
            ("But, as I pointed out, anyone complaining about standing downwind was lying. There was no wind.", 75, True),
            [False, "But, as I pointed out, anyone complaining about standing downwind was lying"]
        ),
        (
            ("I have no notice period on Phobos. I can start immediately.", 50, True),
            [False, "I have no notice period on Phobos. I can start imm"]
        ),
    )
    for key, val in data:
        assert char_check(*key) == val


if __name__ == '__main__':
    test()
