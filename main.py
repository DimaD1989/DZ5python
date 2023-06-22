# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

# my_path = r'C:\Users\d_d19\OneDrive\Рабочий стол\Python\python.txt'
#
# def separate_path(my_path:str) -> tuple():
#     list_my_path = my_path.split('\\')
#     list_last_elem = list_my_path[-1].split('.')
#     path = '\\'.join(list_my_path[0:-1])
#     name = list_last_elem[0]
#     expansion = list_last_elem[-1]
#     return path, name, expansion
#
# print(separate_path(my_path))


# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
#
# names = ['Василий', 'Михаил ', 'Юрий', 'Дмитрий']
# salary = [1700, 2000, 2800, 50000]
# bonus = ['10.25%', '13.00%', '18.50%', '12.05%']
#
# def salary_all(names:list[str],salary:list[int],bonus:list[str]):
#     return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()
# print(salary_all(names,salary,bonus))

# Создайте функцию генератор чисел Фибоначчи(см.Википедию).
def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(20)))
