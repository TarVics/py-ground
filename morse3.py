import re

"""
In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can
be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots"
(short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at
different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can
transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line
periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is
not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a
string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line
exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to
dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some
extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have
trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable
string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).


Eg:
  morseCodes(".--") //to access the morse translation of ".--"
All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip
 checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck!
"""

"""
У цьому каталозі вам потрібно написати декодер азбуки Морзе для дротового електричного телеграфу.
Електричний телеграф працює на 2-провідній лінії за допомогою ключа, який при натисканні з'єднує дроти між собою, що може бути виявлено на віддаленій станції. Азбука Морзе кодує кожен символ, що передається, як послідовність "крапок" (коротких натискань на клавішу) і "тире" (довгих натискань на клавішу).

При передачі азбуки Морзе міжнародний стандарт визначає, що

"Крапка" - має довжину в 1 часову одиницю.
"Тире" - довжиною в 3 одиниці часу.
Пауза між крапками і тире в символі - 1 часова одиниця.
Пауза між символами всередині слова - 3 одиниці часу.
Пауза між словами - 7 одиниць часу.
Однак стандарт не уточнює, яка саме довжина цієї "одиниці часу". І фактично різні оператори будуть передавати з різною швидкістю. Аматору може знадобитися кілька секунд, щоб передати один символ, досвідчений професіонал може передавати 60 слів за хвилину, а роботизовані передавачі можуть працювати набагато швидше.

У цій каталозі ми припускаємо, що прийом повідомлення відбувається автоматично за допомогою обладнання, яке періодично перевіряє лінію, і якщо лінія з'єднана (клавіша на віддаленій станції опущена), записується 1, а якщо лінія не з'єднана (клавіша на віддаленій станції піднята), то записується 0. Після того, як повідомлення буде повністю прийнято, воно потрапляє до вас для декодування у вигляді рядка, що містить лише символи 0 та 1.

Наприклад, повідомлення HEY JUDE, тобто ---- - ---- ---- ---- --- --- - може бути отримано наступним чином:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

Як ви можете бачити, ця передача є абсолютно точною відповідно до стандарту, і апаратне забезпечення дискретизувало лінію рівно два рази на кожну "точку".

Зважаючи на це, ваша задача полягає у реалізації двох функцій:

Функція decodeBits(біти), яка повинна з'ясувати швидкість передачі повідомлення, правильно декодувати повідомлення на крапки, тире і пропуски (один між символами, три між словами) і повернути їх у вигляді рядка. Зауважте, що на початку і в кінці повідомлення можуть зустрічатися зайві 0, переконайтеся, що ви їх ігноруєте. Також, якщо вам важко визначити, чи є певна послідовність одиниць крапкою або тире, вважайте, що це крапка.
2. Функція decodeMorse(morseCode), яка прийме вихідні дані попередньої функції і повертатиме рядок, придатний для читання людиною.

Зауваження: Для кодування слід використовувати символи ASCII . і -, а не символи Unicode.

Таблиця азбуки Морзе попередньо завантажена для вас (див. налаштування рішення, щоб отримати її ідентифікатор вашою мовою).


Наприклад
  morseCodes(".--") //для доступу до азбуки Морзе для ".--"
Всі тестові рядки будуть дійсними до тієї міри, щоб їх можна було надійно декодувати, як описано вище, тому ви можете пропустити перевірку на помилки і винятки, просто зробіть все можливе, щоб з'ясувати, про що йдеться у повідомленні!

Щасти вам!

Translated with www.DeepL.com/Translator (free version)
"""

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', ' ': ' '
}

bits = '000011001100110011000000110000001111110011001111110011111100000000000000110011111100111111001111110000001100110011111100000011111100110011000000110000'


# bits = '110000000000000011'
# bits = '11111100000000000000111111'


def decode_bits(bits_buffer: str) -> list[str]:
    result: list[str] = []

    all_chars: list[str] = re.findall(r'1+|(?<=1)0+(?=1)', bits_buffer)
    if not all_chars:
        return result

    uniq_chars: list[str] = sorted(set(all_chars))

    """
        "Крапка" - має довжину в 1 часову одиницю.
        "Тире" - довжиною в 3 одиниці часу.

        Пауза між крапками і тире в символі - 1 часова одиниця.
        Пауза між символами всередині слова - 3 одиниці часу.
        Пауза між словами - 7 одиниць часу.
    """

    signals: list = [len(chars) for chars in uniq_chars if chars[0] == '1']  # 1*N, 3*N
    pauses: list = [len(chars) for chars in uniq_chars if chars[0] == '0']   # 1*N, 3*N, 7*N

    if pauses:
        if signals[0] > pauses[0]:  # 3*N > 1*N
            signals.insert(0, pauses[0])
        elif signals[0] < pauses[0]:
            if pauses[0] // 7 == signals[0]:            # PAUSES(. . 7*N) -> SIGNALS(1*N .)
                one: int = pauses[0] // 7
                pauses.insert(0, one * 3)
                pauses.insert(0, one)
            elif pauses[0] // 7 == signals[0] // 3:     # PAUSES(. . 7*N) -> SIGNALS(. 3*N)
                one: int = pauses[0] // 7
                signals.insert(0, one)
                pauses.insert(0, one * 3)
                pauses.insert(0, one)
            elif pauses[0] // 3 == signals[0]:          # PAUSES(. 3*N .) -> SIGNALS(1*N .)
                pauses.insert(0, pauses[0] // 3)

    buffer: str = ''

    all_chars_len = len(all_chars)
    pauses_len = len(pauses)

    for k, chars in enumerate(all_chars):
        size = len(chars)
        char = chars[0]

        if char == '1':
            buffer += '.' if size == signals[0] else '-'
            if k + 1 == all_chars_len:
                result.append(buffer)
        elif size > pauses[0]:  # Проміжок між символами чи словами
            result.append(buffer)
            buffer = ''
            if pauses_len > 1 and size > pauses[1]:  # Проміжок між словами
                result.append(' ')

    return result


def decode_morse(morse_data: list[str]):
    print(morse_data)
    result: str = ''
    for char in morse_data:
        result += MORSE_CODE[char]

    return result


morseCode = decode_bits(bits)
message = decode_morse(morseCode)

print(message)  # 'HEY JUDE'
