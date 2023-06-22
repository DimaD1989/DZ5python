# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

my_path = r'C:\Users\d_d19\OneDrive\Рабочий стол\Python\python.txt'

def separate_path(my_path:str) -> tuple():
    list_my_path = my_path.split('\\')
    list_last_elem = list_my_path[-1].split('.')
    path = '\\'.join(list_my_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[-1]
    return path, name, expansion

print(separate_path(my_path))

