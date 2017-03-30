# Программа отбирающая файлы с датой позже чем заданная
import os
from datetime import datetime

# Запрос исходных данных: путь к корневой папке и дата после которой
# были созданы файлы
path = input("Введите путь к иследуемой папке с файлами: ")
date_file = input("Дата последних изменений файлов: ")
# Получаем перечень всех файлов и папок
list_file = list(os.walk(path))
list1 = []
dir1 = []
for rootdir, dirname, file_1 in list_file:

    for file_item in file_1:
        file_path = os.path.join(rootdir, file_item)
        file_2 = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        list1.append(file_2)

print(list1)

# Проходим по всем файлам каждой папки

# дата создания позже заданой даты

# Если да, то сохраняем в файл с путем от корневой паки проекта

# Если нет проверяем следующий файл

# Если папки и файлы закончились, выдаем сообщение об окончании