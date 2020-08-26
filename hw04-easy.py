# Задание-1: Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('Задача 1')
list_1 = [4, 22, 6, 7, 11, 0, 3, 5]
print('list_1:', list_1)
list_2 = list(map(lambda x:x**2, list_1))
print('list_2:', list_2)


# Задание-2: Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('-' * 50)
print('Задача 2')
fruit_list_1 = ['Апельсин', 'Мандарин', 'Яблоко', 'Киви', 'Лимон']
fruit_list_2 = ['Манго', 'Грейпфрут', 'Апельсин', 'Банан', 'Лимон', 'Киви']
result_list = [i for i in fruit_list_1 if i in fruit_list_2]
print(result_list)


# Задание-3: Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('-' * 50)
print('Задача 3')
list_1 = [4, -3, 6, -4, -11, 18, 13, 16, 9, 12, -3, 24, 99, 21]
list_2 = [i for i in list_1 if i >= 0 and i % 4 and not i % 3]
print(list_2)
