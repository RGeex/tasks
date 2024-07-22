"""
Вы мастер расширений файлов? Давайте выясним, проверив, являются ли файлы
Билла изображениями или аудиофайлами. Пожалуйста, используйте регулярное
выражение, если оно доступно на вашем языке.

Вы создадите 2 строковых метода:

    isAudio/is_audio , соответствующий 1 или + заглавным/строчным буквам
    (возможна комбинация), с расширением .mp3, .flac, .alac или .aac.

    isImage/is_image , соответствующий 1 или + заглавным/строчным буквам
    (возможна комбинация), с расширением .jpg, .jpeg, .png, .bmp или .gif.

Обратите внимание, что это не стандартная программа проверки изображений/аудиофайлов.
Предполагается, что это будет проверка только файлов Билла. Билл не любит пунктуацию.
Он тоже не любит цифры. Таким образом, его имена файлов состоят только из букв.

Правила

    Он должен просто возвращать true или false.
    Расширения файлов должны состоять только из строчных букв и цифр.
    Имена файлов должны состоять только из букв (прописных, строчных или обеих букв).
"""


import re


def is_audio(file_name: str) -> bool:
    """
    Проверяет, является ли переданная строка правильным именем файла.
    """
    return bool(re.findall(r'^[a-zA-Z]*.(mp3|flac|alac|aac)$', file_name))


def is_img(file_name: str) -> bool:
    """
    Проверяет, является ли переданная строка правильным именем файла.
    """
    return bool(re.findall(r'^[a-zA-Z]*.(jpg|jpeg|png|bmp|gif)$', file_name))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Nothing Else Matters.mp3", False),
        ("NothingElseMatters.mp3", True),
        ("DaftPunk.FLAC", False),
        ("DaftPunk.flac", True),
        ("AmonTobin.aac", True),
        (" Amon Tobin.alac", False),
        ("tobin.alac", True),
    )
    for key, val in data:
        assert is_audio(key) == val

    data = (
        ("Home.jpg", True),
        ("flat.jpeg", True),
        ("icon.bmp", True),
        ("icon2.jpg", False),
        ("bounce.gif", True),
        ("animate bounce.GIF", False),
        ("transparency.png", True),
    )
    for key, val in data:
        assert is_img(key) == val


if __name__ == '__main__':
    test()
