import json

"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
(Хеш то що зліва записувати не потрібно)
"""


def gmail_reader(file_name: str, tail: str):
    tail_len = len(tail)
    with open(file_name) as src:
        for line in src:
            email = line[line.rindex('\t') + 1:len(line) - 1]
            # email = line.split()[-1]
            if email[-tail_len:] == tail:
                yield email


def file_writer(file_name: str, source) -> None:
    with open(file_name, 'w') as dst:
        for v in source:
            print(v, file=dst)


try:
    reader = gmail_reader('emails.txt', '@gmail.com')
    file_writer('email-gmail.txt', reader)

except Exception as err:
    print(err)

######################################################################################################

"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
 * має бути змога шукати по будь якому полю покупку
 * має бути змога показати найдорожчу покупку
 * має бути можливість видаляти покупку по id
 (ну і меню на це все)
"""


class ShoppingNotebook:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__notes: list[dict] = []
        self._read_notes()

        gen_id: int = max(self.__notes, key=lambda note: note['id'])['id'] + 1 if self.__notes else 1
        self.__id = self.__genid(gen_id)

    @staticmethod
    def __genid(init: int = 1):
        current = init
        while True:
            yield current
            current += 1

    def _read_notes(self) -> None:
        try:
            with open(self.__file_name) as file:
                self.__notes = json.load(file)
        except (Exception,):
            self.__notes = []

    def _write_notes(self) -> None:
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__notes, file)
        except Exception as ex:
            print(ex)

    # * вивід всіх покупок
    def show_all(self) -> None:
        for note in self.__notes:
            print(note)

    # * має бути змога додавати покупку в книгу
    def add_new(self, name: str, price: float) -> None:
        self.__notes.append({'id': next(self.__id), 'name': name, 'price': price})
        self._write_notes()

    # * має бути змога шукати по будь якому полю покупку
    def find_by(self, name: str, value: str) -> dict | None:
        return next((note for note in self.__notes if str(note[name]) == value), None)

    # * має бути змога показати найдорожчу покупку
    def find_expensive(self) -> dict | None:
        return max(self.__notes, key=lambda note: note["id"])

    # * має бути можливість видаляти покупку по id
    def delete_note(self, note_id: int) -> None:
        self.__notes = [note for note in self.__notes if note['id'] != note_id]
        self._write_notes()

    def run(self):
        while True:
            print('1. вивід всіх покупок')
            print('2. має бути змога додавати покупку в книгу')
            print('3. має бути змога шукати по будь якому полю покупку')
            print('4. має бути змога показати найдорожчу покупку')
            print('5. має бути можливість видаляти покупку по id')
            print('6. вихід')

            choice = input('Виберіть номер операції: ')

            try:
                match choice:
                    case '1':
                        self.show_all()
                    case '2':
                        name: str = input('Вкажіть назву покупки: ')
                        while True:
                            try:
                                price: float = float(input('Вкажіть ціну покупки: '))
                                break
                            except (Exception,):
                                pass

                        self.add_new(name, price)
                    case '3':
                        name: str = ''
                        while name not in ['id', 'name', 'price']:
                            name: str = input('Вкажіть назву поля для пошуку (id | name | price): ')

                        value = input(f'Вкажіть значення поля {name} покупки: ')

                        result = self.find_by(name, value)

                        print(f'Результат пошуку: {result}')
                    case '4':
                        expensive = self.find_expensive()
                        print(f'Най дорожча покупка: {expensive}')
                    case '5':
                        product_id: int = int(input('Вкажіть значення поля id для видалення покупки: '))
                        self.delete_note(product_id)
                    case '6':
                        break

            except Exception:
                pass


book_notes = ShoppingNotebook('books.json')
book_notes.run()

######################################################################################################

"""
*********Кому буде замало ось завдання з співбесіди
Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку 
то брати наступне з того ж підсписку

в результат має записатись тільки 5 id

з даним списком мае вийти ось такий результат:
res = [1110, 1120, 1130, 1111, 1122]

"""

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


# res: list[int] = []
#
# while data and len(res) < 5:
#     items = data.pop(0)
#
#     while items:
#         id = items.pop(0)["id"]
#
#         if id not in res:
#             res.append(id)
#             data.append(items)
#             break
#
# print(res)

def make() -> list[int]:
    res: list[int] = []
    gens: list = [(v["id"] for v in items if v["id"] not in res) for items in data]
    while True:
        for gen in gens:
            res.append(next(gen))
            if len(res) == 5:
                return res


print(make())

######################################################################################################
