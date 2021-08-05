# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

data = input(' Введите список 6 слов или чисел через пробел: ')
list = data.split()
if len(list) > 5:
    print('Слишком длинный список')

if len(list) % 2 > 0:
    last = list.pop()
    list[0], list[1], list[2], list[3], list[4], list[5] = list[1], list[0], list[3], list[2], list[5], list[4]
    list.append(last)
else:
    list[0], list[1], list[2], list[3], list[4], list[5] = list[1], list[0], list[3], list[2], list[5], list[4]
print(list)
