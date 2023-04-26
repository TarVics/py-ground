'''
ddwede
'''

"""
wswssws
"""

# wdedwedwed

############################################################

# print("Hello World !!")
# print(1, 2, 3, sep='|', end='<EOL>\n')
#
# i = 3
# f = 3.14
# b = True  # or False
# s = 'string'  # or "string"
# n = None  #
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# int1 = int(f)
# print(type(int1))
# print(int1)
#
# a = b = c = 10
# print(a, b, c)
#
# # int()
# # str()
# # float()
# # bool()
#
# print(bool(1), bool(1.5), bool(0), bool(""), bool("sss"))

############################################################

# a = 0
# a += 1
# print(a)
#
# a = a + 2
# print(a)

############################################################

# a = 5
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)  # Ціло численне ділення
# print(a % b)  # Залишок від ділення
# print(a ** b)  # Приведення до степеня
#
# print(2525 ** 2525)  # Великі числа

# num = input('Enter num: ')
# inum = int(num)
# print(num, inum, sep=', ')
# print(type(num), type(inum), sep=', ')

############################################################

# Boolean операції

# a = 2
# b = 3
#
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)
# print(a == b)
# print('&&&', a is b)
# print(a != b)
# print('!!!', a is not b)
#
# print('isinstance str "123" =', isinstance('123', str))
# print('isinstance int 1 = ', isinstance(1, int))

############################################################

# num = int(input("Enter number: "))
# if num == 0:
#     print("Num is equal to 0")
# elif num == 1 or num == 2:
#     print("Num = 1 or 2")
# elif num == 3 and num > 0:
#     print("Num = 3 and > 0")
# elif num in [5, 6, 7, 8, 9]:
#     print("Num in 5, 6, 7, 8, 9")
# elif num is 15:
#     print("Num is 15")
# elif num > 5 and num is not 15:
#     print("Num is greater than 5")
# # elif num:
# #     print("Num is not 0")
# # elif not num:
# #     print("Num is 0")
# else:
#     print("Num is less or equal than 5")

############################################################

# num = int(input("Enter number: "))
# res = 'yes' if num > 5 else 'no'  # Тернарний оператор
# print(res)


############################################################

# Lists

# l = [1, 2, 3, 4, 5, '232']
# print(l, l[0], l[-1])
#
# l[0] = 111
# print(l, len(l))
#
# l.append(True)
# print(l, ':', len(l))
#
# del l[0]
# print(l, 'DEL', len(l))
#
# l2 = l
# l2[0] = 'SSS'
# print(l, 'SET', len(l))
#
# l3 = l.copy()
# print(l3, 'COPY', len(l3))

# l = [1, 2, 3]
# l.insert(1, '|')
# print(l)
#
# l.insert(1000, '<EOL>')
# print(l)
#
# l.insert(-1, 'PREV')
# print(l)

# l = [1, 2, 3, 1, 1]
# l.remove(1)  # Шукає значення і видаляє
# print(l)
#
# l.remove(1)  # Шукає значення і видаляє
# print(l)
#

# l = [1, 2, 3]
# l.pop()  # Видалити останній елемент зі списку
# print(l)
# print(l.pop(0))  # Вертає видалений елемент

# l = [1, 2, 3]
# l2 = [4, 5, 6]
# #l.extend(l2)
# #l += l2
# l = l + l2
# print(l)  # Розширення/зливання списків

# l = [1, 2, 3, 2]
# # i = l.index(2)  # Пошук значення
# i = l.index(2, 2)  # Пошук значення починаючи з позиції
# print(l, 'index of 2 =', i)

# l = [1, 2, 3, 2]
# l.reverse()
# print(l)
#
# l.sort() # Сортує масив
# print(l)
#
# l.sort(reverse=True)
# print(l)
#
#

# l = [1, 2, 3, 2]
# print(l.count(2))  # Порахувати кількість значень в масиві які рівні заданому параметру

# l = [1, 2, 3, 2]
# l.clear()
# print(l)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# print(l[0:2])  # Зріз масиву
# print(l[:2])  # Зріз масиву те ж саме
# print(l[0:5:2])  # Зріз масиву із кроком 2
# print(l[:5:2])  # Зріз масиву із кроком 2
# print(l[::2])  # Зріз усього масиву із кроком 2
# print(l[::-1])  # Зріз усього масиву із кроком 1 але в зворотньому порядку
# print(l[::-2])  # Зріз усього масиву із кроком 2 але в зворотньому порядку

# s = '1234'
# l = list(s)   # Аналог split
# print(l)

# tuple - кортежі
# my_tuple = (1, 2, 3, 4, 5, 2, 2)
# print(my_tuple[1])
#
# # del my_tuple[1] # Видаляти заборонено
#
# print(my_tuple.count(2))  # Порахувати кількість заданих значень у параметрі
# print(my_tuple.index(2, 3))  # Знайти значення
#

# dict

# my_typle = (1,2,3)

# user = {
#     'name': "1234",
#     1: "1234",
#     None: 12,
#     True: 44,
#     False: 449,
#     (1,2,3,4): 442,
#     my_typle: "typle"
# }
#
# print(user)
# print(user['name'], user[my_typle])
# print(user.get('name'))
# print(user.get('name1'))  # Якщо ключа нема, то верне None
# print(user.get('name1', '<None>'))  # Якщо ключа нема, то верне None

# del user[my_typle]
# user.pop(my_typle)
# user.pop(my_typle, None)    # У випадку, якщо ключ відсутні, то поверне значенне, задане у параметрі
# print(user)
# user.clear()
# print(user)
# u = user.popitem()  # Видалить останній елемент
# print(user, '->', u)

# user2 = user.copy()
# print(user2)

# items = user.items();
# print(items)
# print(list(items))
#
# print(list(user.keys()))
# print(list(user.values()))

# user = {
#     'name': 'max',
#     'age': 15,
# }
#
# user.setdefault('age', 25)
# user.setdefault('age2', 25)
# print(user)
#
# # user.update({'street': 'street'})
# user |= {'street': 'street'}
# print(user)

# user = dict(name='max', age=15)
# print(user)

###########################################################

# SET

# l = [1, 2, 3, 4, 6, 2, 3, 1, 3]
#
# s = set(l)
# print(s)
#
# s = {1,2,3,4,5,1,5,3}
# print(s)
#
# s = {}  # dict
# s = set()   # set
# # print(s)
# # print(type(s))
# s.add(3)
# s.add(6)
# s.add(22)
# s.add(22)
# s.add(3)
# print(s)
#
# print(len(s))
# print(list(s))
#

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 4, 3}
# print(set1.issuperset(set2))  # Чи включає множина 1 множину 2
# print(set1.issubset(set2))  # Чи є множина 1 підмножиною 2
# print(set1.isdisjoint(set2))  # Множина 1 немає спільних елементів
# print(set1.isdisjoint({7, 8, 9}))  # Множина 1 немає спільних елементів
# print(set1.union({7, 8, 9}))  # Злиття множин. Злита множина повертається як результат
# print(set1.intersection(set2))  # Спільні елементи множини
# print(set1.difference(set2))  # Виключення з множини 1 спільних елементів із множиною 2
# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 1}
# print(set1.symmetric_difference(set2))  # Виключення з множини 1 спільних елементів із множиною 2
#                                         #  + Виключення з множини 2 спільних елементів із множиною 1
#
# set1.update(set2)   # Оновлює множину 1 значеннями із множини 2
# print(set1)
# #set1.remove(22)     # Видалення значення 22. Помилка, якщо елемент відсутній
# set1.discard(222)   # Видалення значення 22. Помилка відсутня, якщо елемент відсутній
# print(set1)
# pop = set1.pop()    # Видалення наступного елемента множини
# print(set1)
# pop = set1.pop()
# print(set1)
#

###############################################################################
# strings

# st = '-'*20
# print(st)

string = "hello, my name is Max, I\"m 18 and my weight 70.5 kg"

#
# name = 'Max'
# age = 18
# weight = 70.5
#
# string = "Hello, my name is Max, I`m 18 and my weight 70.5 kg"
# string = "Hello, my name is " + name + ", I`m " + str(age) + " and my weight " + str(weight) + " kg"
# string = "Hello, my name is %s, I`m %i and my weight %f kg" % (name, age, weight)
# string = "Hello, my name is {}, I`m {} and my weight {} kg".format(name, age, weight)
# string = "Hello, my name is {name}, I`m {age} and my weight {weight} kg".format(age=age, name=name, weight=weight)
# string = f"hello, my name is {name}, I`m {age} and my weight {weight} kg"

# print(string)
# print(string.index('na'))  # Пошук словосполучення. Якщо нема, то помилка
# print(string.index('na', 1))  # Пошук словосполучення, починаючи з позиції. Якщо нема, то помилка
# print(string.find('l', 1))  # Пошук словосполучення. Якщо нема, то -1
# print(string.find('l', 1))  # Пошук словосполучення, починаючи з позиції. Якщо нема, то -1
# print(string.count('l'))  # Підрахунок входжень словосполучень
# print(string.capitalize())  # Текст з великої літери. Всі інші літери - маленькі
# print(string.upper())  # Текст великими літерами
# string = string.lower()  # Текст маленькими літерами
# print(string)
# print(string.islower())  # Чи є весь текст маленькими літерами
# print(string.isupper())  # Чи є весь текст великими літерами
# print('hello world'.title())  # Кожне слово починається з великої літери
# print('Hello World'.swapcase())  # Інверсія регістру символів
# print('asd', 'asd'.isalpha())  # Перевірка чи усі символи
# print('12s', '12s'.isdigit())  # Перевірка чи усі цифри
# print('12s ', '12s '.isalnum())  # Перевірка чи усі символи + цифри
# print('12sЇ', '12sЇ'.isalnum())  # Перевірка чи усі символи + цифри
# print('hello'.startswith('e'))  # Починається з
# print('hello'.endswith('lo'))  # Закінчується з

# print(['    aa aa         '.strip()])  # Забирає пробіли з кінців
# print(['dd    aa aa         dd'.strip('d ')])  # Забирає пробільні символи з кінців
# print(['    aaaa         '.lstrip()])  # Забирає пробіли ліворуч
# print(['    aaaa         '.rstrip()])  # Забирає пробіли праворуч
# print('hello world hello'.split(' '))  # Формує масив, розділюючи стрічку роздільниками
# print('hello-world-hello'.split('-'))  # Формує масив, розділюючи стрічку роздільниками
# print('hello is hello'.partition('ll'))   # Формує кортеж із трьох елементів:
#                                           # 1. Значення до роздільника, 2. роздільник, 3. Значення після роздільника

# l = ['hello', 'car', 'one']
# print('-'.join(l))  # Злиття масиву у стрічку через поділювач
# print(''.join(l))  # Злиття масиву у стрічку через поділювач

# print('  d   '.isspace())  # Чи є лише пробільні символи
# print('hello world hello'.replace('l', 'L', 3))  # Заміна тексту + кількість замін, які потрібно виконати

# print('hello world hello'[::2])  # Зріз тексту. Забираємо кожен 2 символ
#
# print(min([6, 1, 2, 3, 4]))  # Мінімальне значення
# print(min(6, 1, 2, 3, 4))  # Мінімальне значення
# print(max([6, 1, 2, 3, 4]))  # Максимальне значення
# print(max(6, 1, 2, 3, 4))  # Максимальне значення
# print(sorted([2, 1, 3, 2, 1]))  # Повертає відсортований масив. Вхідний масив не змінює
# print(sorted([2, 1, 3, 2, 1], reverse=True))  # Відсортований масив у зворотному порядку
# print(pow(25, 25))  # Степінь числа

########################################################################################
# Функції

# def func():
#     print('Hello')
#
# func()


# def func2(a, b, c=3, *args, **kwargs):
#     print(a + b + c)
#     print(args)
#
#     print(kwargs)
#
# func2(1, 2, 5, 3, 5, 6, 7, age=34, name='Max')

# l = [1, 2]
#
#
# def func(a, b):
#     print(a, b)
#     return 12345
#
#
# print(func(*l))
#
# i = 5
# while i > 0:
#     i -= 1
#     print(i)
# else:
#     print('finish')

# l = [33, 66, 88, 1, 3, 7, 8]
#
# for i in l:
#     print(i)
#
# for i, item in enumerate(l):
#     print(i, item, sep='-')
#
# for i in range(10):
#     print(i)
#

# s = 'asdfg'
# for i, ch in enumerate(s):
#     print(i, ch)

# for i in range(5, 10, 2):  # from 5 to 10-1, step 2
#     print(i)

# user = {
#     'name': 'max',
#     'age': 18
# }

# for key in user.keys():
#     print(key)
#
# for key in user.values():
#     print(key)

# for k, v in user.items():
#     print(f'{k=} - {v=}')

#
# l = [i for i in range(5)]
#
# print(l)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
#
# res = [i for i in l if i % 2 == 0] # Comprehension
# res = [str(i) for i in l if i % 2 == 0]
# res = [i**2 for i in l if i % 2 == 0]
# res = [i if i != 6 else i + 1 for i in l if i % 2 == 0]
# res = [i if i != 6 else 'ops' for i in l if i % 2 == 0]
#
# print(res)

# dict1 = {'NaMe': 'Max', 'aGe': 19}
#
# res = {k.lower(): v for k, v in dict1.items()}
#
# print(res)

l = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]

res = [i for j in l for i in j]
print(res)

res = []
for j in l:
    for i in j:
        res.append(i)

print(res)

