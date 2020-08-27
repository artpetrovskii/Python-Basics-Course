# Задача-1: Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py

import os
import hw05_easy as hw5

def dir_change(path):
    try:
        os.chdir(path)
        print(f"Переход в папку {path}")
    except FileNotFoundError:
        print(f"Папка dir_{path} не создана")


def menu():
    answer = ''
    while answer != 5:
        answer = input("Выберите действие:\n"
                       "1. Перейти в папку\n"
                       "2. Просмотреть содержимое текущей папки\n"
                       "3. Удалить папку\n"
                       "4. Создать папку\n"
                       "5. Выход\n")

        if answer == '1':
            path_name = input("Укажите папку для перехода: ")
            print(dir_change(path_name))
        elif answer == '2':
            hw5.list_dir()
        elif answer == '3':
            path_name = input("Введите имя папки для удаления: ")
            hw5.del_dir(path_name)
        elif answer == '4':
            path_name = input("Введите имя новой папки: ")
            hw5.make_dir(path_name)
        elif answer == '5':
            break
        else:
            print("Введено некорректное значение. Пожалуйста, повторите")

if __name__ == '__main__':
    menu()
