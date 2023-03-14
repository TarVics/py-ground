import json

"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
(Хеш то що зліва записувати не потрібно)
"""


def gmail_reader(file_name: str, tail: str):
    tail_len = len(tail)
    with open(file_name) as src:
        for line in src:
            res = line[line.rindex('\t') + 1:len(line) - 1]
            if res[-tail_len:] == tail:
                yield res


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

    def _read_notes(self) -> list[dict]:
        notes: list[dict] = []

        try:
            with open(self.__file_name) as file:
                notes = json.load(file)
        except Exception:
            pass

        return notes

    def _write_notes(self, notes: list[dict]) -> None:
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(notes, file)
        except Exception as ex:
            print(ex)

    # * вивід всіх покупок
    def show_all(self) -> None:
        notes: list[dict] = self._read_notes()
        for note in notes:
            print(note)

    # * має бути змога додавати покупку в книгу
    def add_new(self, id: int, name: str, price: float) -> None:
        notes: list[dict] = self._read_notes()
        notes.append({'id': id, 'name': name, 'price': price})
        self._write_notes(notes)

    # * має бути змога шукати по будь якому полю покупку
    def find_by(self, name: str, value: any) -> dict | None:
        notes: list[dict] = self._read_notes()
        return next((note for note in notes if note[name] == value), None)

    # * має бути змога показати найдорожчу покупку
    def find_expensive(self) -> dict | None:
        books: list[dict] = self._read_notes()
        if len(books) == 0:
            return None

        current_book = books[0];

        for book in books:
            if book['price'] > current_book['price']:
                current_book = book

        return current_book

    # * має бути можливість видаляти покупку по id
    def delete_book(self, id: int) -> None:
        books: list[dict] = self._read_notes()
        self._write_notes([book for book in books if book['id'] != id])

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
                        id: int = int(input('Вкажіть id книги: '))
                        name: str = input('Вкажіть name книги: ')
                        price: float = float(input('Вкажіть price книги: '))
                        self.add_new(id, name, price)
                    case '3':
                        name: str = input('Вкажіть назву поля (id | name | price): ')
                        value = input(f'Вкажіть значення поля {name} книги: ')
                        res = self.find_by(name, value)
                        print(f'Знайдена книга {res}')
                    case '4':
                        res = self.find_expensive()
                        print(f'Знайдена найдорожча книга {res}')
                    case '5':
                        id: str = input('Вкажіть значення поля id для видалення книги: ')
                        self.delete_book(id)
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

res: list[int] = []

while data:
    items = data.pop(0)

    while items:
        id = items.pop(0)["id"]

        if not next((v for v in res if v == id), None):
            res.append(id)
            data.append(items)
            break

print(res)
######################################################################################################
