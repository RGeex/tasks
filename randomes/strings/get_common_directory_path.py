"""
Возвращает общий путь к каталогу для указанного массива полных имен файлов.

 @param {array} pathes
 @return {string}

Примеры:

  ['/web/images/image1.png', '/web/images/image2.png']  => '/web/images/'
  ['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf'] => ''
  ['/web/assets/style.css', '/.bin/mocha',  '/read.me'] => '/'
  ['/web/favicon.ico', '/web-scripts/dump', '/webalizer/logs'] => '/'

(с)RSS
"""


import re


def get_common_directory_path(pathes: list[str]) -> str:
    """
    Поиск общего пути для заданный файлов.
    """
    res = []
    for x in zip(*[re.findall(r'(.*?/)', x) for x in pathes]):
        if len(set(x)) > 1:
            break
        res.append(x[0])
    return ''.join(res)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (['/web/images/image1.png', '/web/images/image2.png'], '/web/images/'),
        (['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf'], ''),
        (['/web/assets/style.css', '/.bin/mocha',  '/read.me'], '/'),
        (['/web/favicon.ico', '/web-scripts/dump', '/webalizer/logs'], '/'),
    )
    for key, val in data:
        assert get_common_directory_path(key) == val


if __name__ == '__main__':
    test()
