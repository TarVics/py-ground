from abc import ABC, abstractmethod

"""
# ДЗ
"""

"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін
"""


class Rectangle:

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self.__s = x * y

    def __repr__(self) -> str:
        return f'Rectangle({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'{{x:{self.x}, y: {self.y}}}'

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int) -> None:
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int) -> None:
        self.__y = y

    # + сумма площин двох екземплярів ксласу
    def __add__(self, other) -> int:
        return self.__s + other.__s

    # - різниця площин двох екземплярів ксласу
    def __sub__(self, other) -> int:
        return self.__s - other.__s

    # == площин на рівність
    def __eq__(self, other) -> bool:
        return self.__s == other.__s

    # != площин на не рівність
    def __neq__(self, other) -> bool:
        return self.__s != other.__s

    # >, < меньше більше
    def __gt__(self, other) -> bool:
        return self.__s > other.__s

    def __ge__(self, other) -> bool:
        return self.__s >= other.__s

    def __lt__(self, other) -> bool:
        return self.__s < other.__s

    def __le__(self, other) -> bool:
        return self.__s <= other.__s

    # при виклику метода len() підраховувати сумму сторін
    def __len__(self) -> int:
        return (self.__x + self.__y) * 2


r1 = Rectangle(2, 3)
r2 = Rectangle(4, 5)

print(f'{r1=}')
print(f'{r2=}')

# + сумма площин двох екземплярів ксласу
print(f'r1 + r2 = {r1 + r2}')

# - різниця площин двох екземплярів ксласу
print(f'r1 - r2 = {r1 - r2}')

# == площин на рівність
print(f'r1 == r2 = {r1 == r2}')

# != площин на не рівність
print(f'r1 != r2 = {r1 != r2}')

# >, < меньше більше
print(f'r1 < r2 = {r1 < r2}')
print(f'r1 > r2 = {r1 > r2}')

# при виклику метода len() підраховувати сумму сторін
print(f'len(r1) = {len(r1)}')
print(f'len(r2) = {len(r2)}')

print('*' * 70)

###############################################################################

"""
створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, 
  та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення

"""


class Human:

    def __init__(self, name: str, age: int) -> None:
        self.__age = age
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def name(self) -> str:
        return self.__name


class Cinderella(Human):
    __count: int = 0

    def __init__(self, name: str, age: int, size: int) -> None:
        super().__init__(name, age)
        self.__size = size
        Cinderella.__count += 1

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.age}, {self.size})'

    def __str__(self):
        return f'{{name:{self.name}, age: {self.age}, size: {self.size}}}'

    @classmethod
    def count_instances(cls) -> int:
        return cls.__count

    @property
    def size(self) -> int:
        return self.__size


class Prince(Human):

    def __init__(self, name, age, size) -> None:
        super().__init__(name, age)
        self.__size = size

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.age}, {self.size})'

    def __str__(self) -> str:
        # return f'{self.__dict__}'
        return f'{{name:{self.name}, age: {self.age}, size: {self.size}}}'

    @property
    def size(self) -> int:
        return self.__size

    def find_cinderella(self, items: list[Cinderella]) -> Cinderella | None:
        for c in items:
            if c.size == self.__size:
                return c
        else:
            return None


prince = Prince('Prince', 18, 36)
print(prince)

cinderellas = [Cinderella('c1', 18, 45), Cinderella('c2', 28, 41), Cinderella('c3', 28, 36)]
print(cinderellas)
print('count_instances', Cinderella.count_instances())

print('finded = ', prince.find_cinderella(cinderellas))

print('*' * 70)

###############################################################################

"""
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом 
  Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

Приклад:

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()

для перевірки ксассів використовуємо метод isinstance, приклад:

user = User('Max', 15)
shape = Shape()

isinstance(max, User) -> True
isinstance(shape, User) -> False

"""


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()


class Printable(ABC):

    @abstractmethod
    def print(self) -> None:
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

class Book(Printable):

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self) -> str:
        return f'{{name:{self.name}}}'

    def print(self):
        print(self)

    def __init__(self, name):
        self.name = name


class Magazine(Printable):

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self) -> str:
        return f'{{name:{self.name}}}'

    def __init__(self, name) -> None:
        self.name = name

    def print(self) -> None:
        print(self)


# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і
# робити перевірку чи то що передають є класом
#   Book або Magazine инакше ігрнорувати додавання

class Main:

    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, printable: Printable) -> None:
        if isinstance(printable, (Magazine, Book)):
            cls.__printable_list.append(printable)

    # - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
    @classmethod
    def show_all_magazines(cls) -> None:
        for m in cls.__printable_list:
            if isinstance(m, Magazine):
                print(m)

    # - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
    @classmethod
    def show_all_books(cls) -> None:
        for m in cls.__printable_list:
            if isinstance(m, Book):
                print(m)


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
