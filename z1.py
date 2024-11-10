#2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
import os
def get_absolute_path(path):
    *_, extension = os.path.splitext(path)
    path_to, _ = os.path.split(path)
    file_name = os.path.basename(path).split('.')[0]
    
    return path_to, file_name, extension


if __name__ == '__main__':
    path = 'c:/Users/pc/Desktop/geek/3/python/hw5/ttt.txt'
    print(get_absolute_path(path))