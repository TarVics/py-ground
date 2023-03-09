"""
    strings
"""

"""
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
"""

# st = input("Введіть строку: ")
#
# if st == "":
#     st = 'as 23 fdfdg544'
#
# l = list(st)
# l2 = [c for c in l if c.isdigit()]
#
# print(','.join(l2))

"""
2)написати прогу яка вибирає зі введеної строки числа і виводить їх
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
"""

# st = input("Введіть строку: ")
#
# if st == "":
#     st = 'as 23 fdfdg544 34'
#
# res = []
# curr = ''
#
# for c in st:
#     if c.isdigit():
#         curr += c
#     elif curr != '':
#         res.append(curr)
#         curr = ''
# else:
#     if curr != '':
#         res.append(curr)
#
# print(', '.join(res))

################################################################################################

"""
    list comprehension
"""

"""
1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
"""

# greeting = 'Hello, world'
# l = [c.upper() for c in greeting]
# print(l)

"""
2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
"""

# l = [i ** 2 for i in range(50) if i % 2]
# print(l)

################################################################################################

"""
function
"""

"""
- створити функцію яка виводить ліст
"""

# def show_list(l):
#     print(*l, sep=', ')
#
#
# l = [1, 2, 3, 4, 5]
#
# show_list(l)

"""
- створити функцію яка приймає три числа та виводить та повертає найбільше.
"""

# def input_max(d1,d2,d3):
#     print('Найбільше:', max(d1, d2, d3))
#
#d1 = int(input("Введіть число 1: "))
#d2 = int(input("Введіть число 2: "))
#d3 = int(input("Введіть число 3: "))
#
#input_max(d1, d2, d3)

"""
- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
"""

# def get_least(*args):
#     print('MAX: ', max(args))
#     return min(args)
#
#
# least = get_least(9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -10)
#
# print('MIN: ', least)

"""
- створити функцію яка повертає найбільше число з ліста
"""

# def get_max(*args):
#     return max(*args)
#
#
# l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -10]
#
# print('MAX: ', get_max(l))


"""
- створити функцію яка повертає найменьше число з ліста
"""

# def get_min(*args):
#     return min(*args)
#
#
# l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -10]
#
# print('MIN: ', get_min(l))

"""
- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
"""

# l = [4, 3, 2, 1]
#
# def list_summ(l):
#     result = 0
#     for d in l:
#         result += d
#     return result
#     #return summ(l)
#
#
# print(list_summ(l))

"""
- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
"""

# l = [4, 3, 2, 1]
#
# def list_avg(l):
#     result = 0
#     for d in l:
#         result += d
#     return result / len(l)
#
#
# print(list_avg(l))

################################################################################################

"""
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - знайти мін число
  - видалити усі дублікати
  - замінити кожне 4-те значення на 'X'
"""

# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# print('MIN: ', min(l))
#
# list2 = set(l)
# print(list(list2))
#
# list3 = [v if (k+1) % 4 != 0 else 'X' for k, v in enumerate(l)]
# print(list3)

"""
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
"""

# def show_square(size):
#     print('*' * size)
#     x = '*' + ' ' * (size - 2) + '*'
#     for i in range(size - 2):
#         print(x)
#     print('*' * size)
#
#
# show_square(4)

"""
3) вывести табличку множення за допомогою цикла while
"""

# def show_table():
#     r = 1
#     while r < 10:
#         l = []
#         c = 1
#         while c < 10:
#             l.append(str(r * c))
#             c += 1
#
#         r += 1
#         print('\t'.join(l))
#
#
# show_table()

"""
4) переробити це завдання під меню
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 7, 9]


def list_avg(l):
    result = 0
    for d in l:
        result += d
    return result / len(l)


def choose():
    res = ''
    while res not in ('1', '2', '3', '4', '6'):
        print("1. знайти мін число")
        print("2. видалити усі дублікати")
        print("3. замінити кожне 4-те значення на 'X'")
        print("4. вивести елемент листа, значення якого найближче до середьно арифметичному усіх чисел")
        print("6. вихід")

        res = input("Зробіть ваш вибір: ")

    return res


op = ''
while op != '6':
    op = choose()
    if op == '1':
        print(l)
        print('min_num:', min(l))
    if op == '2':
        print(l)
        print('del_bubl:', list(set(l)))
    if op == '3':
        print(l)
        l4 = [v if (k + 1) % 4 else 'X' for k, v in enumerate(l)]
        print(l4)
    if op == '4':
        print(l)
        avg = list_avg(l)
        print('avg: ', avg)
        l4 = [avg - i if avg > i else i - avg for i in l]
        idx = 0
        for k, v in enumerate(l4):
            idx = k if v < l4[idx] else idx

        print("RESULT", l[idx])
