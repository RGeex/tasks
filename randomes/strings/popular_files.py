"""
В последнее время вы работаете с множеством различных типов файлов,
поскольку ваши интересы расширились.

Но какие типы файлов вы используете чаще всего? Учитывая этот вопрос,
мы рассмотрим следующую проблему.

Учитывая List/Array имён файлов (строки) files вернуть
List/Array of string(s)содержащий наиболее распространенные расширения.
Если есть связь, верните отсортированный список всех расширений.
Важная информация:

    Не забывайте, что вы работали с множеством разных типов файлов, поэтому
    ожидайте интересных расширений/имен/длин файлов в случайных тестах.
    Имена файлов и расширения будут содержать только буквы (с учетом регистра)
    и цифры.
    Если файл имеет несколько расширений (например: mysong.mp3.als) учитывайте
    только последнее расширение ( .als в этом случае)

Примеры

files = ['Lakey - Better days.mp3', 
         'Wheathan - Superlove.wav', 
         'groovy jam.als', 
         '#4 final mixdown.als', 
         'album cover.ps', 
         'good nights.mp3']

вернулся бы: ['.als', '.mp3'], поскольку оба расширения встречаются в файлах
два раза.

files = ['Lakey - Better days.mp3', 
         'Fisher - Stop it.mp3', 
         'Fisher - Losing it.mp3', 
         '#4 final mixdown.als', 
         'album cover.ps', 
         'good nights.mp3']

вернусь ['.mp3'], потому что оно появляется больше раз, чем любое другое
расширение, и ни одно другое расширение не встречается столько же раз.
"""


def popular_files(files: list[str]):
    """
    Поиск среди списка файлов, самых используемых форматов.
    """
    tmp, res = {}, {}
    for file in files:
        x = f".{file.rsplit('.')[-1]}"
        tmp[x] = tmp.get(x, 0) + 1
    for k, v in tmp.items():
        res[v] = res.get(v, []) + [k]
    
    return sorted(max(res.items(), default=[[]])[-1])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            ['Lakey - Better days.mp3', 'Wheathan - Superlove.wav', 'groovy jam.als', '#4 final mixdown.als', 'album cover.ps', 'good nights.mp3'],
            ['.als', '.mp3']
        ),
        (
            ['Lakey - Better days.mp3', 'Fisher - Stop it.mp3', 'Fisher - Losing it.mp3', '#4 final mixdown.als', 'album cover.ps', 'good nights.mp3'],
            ['.mp3']
        ),
        ([],[]),
    )
    for key, val in data:
        assert popular_files(key) == val


if __name__ == '__main__':
    test()
