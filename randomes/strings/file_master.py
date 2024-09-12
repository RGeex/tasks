"""
Задача:
Эта ката требует от вас написать объект, который получает путь к файлу. и
выполняет над ним операции. ПРИМЕЧАНИЕ ДЛЯ ПОЛЬЗОВАТЕЛЕЙ PYTHON . Вы не
можете использовать модули os.path, glob и re.
Целью этого ката является использование синтаксического анализа строк, поэтому
вам не нужно импортировать внешние библиотеки.
Тестирование:

Питон:

>>> master = FileMaster('/Users/person1/Pictures/house.png')
>>> master.extension()
'png'
>>> master.filename()
'house'
>>> master.dirpath()
'/Users/person1/Pictures/'

"""


class FileMaster():
    """
    Анализирует переданную строку разделяя ее на путь до файла, название файла и его расширение.
    Не используя внешние библиотеки.
    """
    def __init__(self, filepath) -> None:
        self.path, (self.file, self.ext) = [x.rsplit('.', 1) if i else f'{x}/' for i, x in enumerate(filepath.rsplit('/', 1))]
    
    def extension(self):
        """
        Расширение файла.
        """
        return self.ext
    
    def filename(self):
        """
        Имя файла.
        """
        return self.file
    
    def dirpath(self):
        """
        Путь до файла.
        """
        return self.path


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    master = FileMaster('/Users/person1/Pictures/house.png')
    data = (
        (master.extension(), 'png'),
        (master.filename(), 'house'),
        (master.dirpath(), '/Users/person1/Pictures/'),
    )
    for key, val in data:
        assert key == val


if __name__ == '__main__':
    test()
