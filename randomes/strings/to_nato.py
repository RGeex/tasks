"""
Задача

Вам придется перевести строку в алфавит пилота ( фонетический алфавит НАТО ).

Вход:

If, you can read?

Выход:

India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Примечание:

    Существует предварительно загруженный словарь, который вы можете использовать, с именем NATO.
    Он использует клавиши верхнего регистра, например NATO['A']является "Alfa". См.
    комментарии в исходном коде, чтобы узнать, как получить к нему доступ на вашем языке.
    Набор используемых знаков препинания ,.!?.
    В возвращаемой строке следует сохранять знаки препинания, но не пробелы.
    Рентгеновский снимок не должен иметь черточки внутри.
    Каждое слово и знак препинания должны быть разделены пробелом.
    Не должно быть никаких пробелов в конце

"""

db = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
    'Z': 'Zulu'
}


def to_nato(words: str) -> str:
    """
    Расшифровка строки (NATO).
    """
    return ' '.join(db.get(w.upper(), w) for w in words if not w.isspace())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("If you can read", "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"),
        ("Did not see that coming", "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"),
        (".d?d!", ". Delta ? Delta !")
    )
    for key, val in data:
        assert to_nato(key) == val


if __name__ == '__main__':
    test()
