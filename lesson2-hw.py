from typing import Callable, Any

"""
1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
"""
"""
2) протипізувати перше завдання
"""

print(' [TASK 1,2] '.center(70, '-'))

NotebookType = tuple[Callable[[str], None], Callable[[], list[str]]]


def notebook() -> NotebookType:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return [*todo_list]

    return add_todo, get_all


add_todo, get_all = notebook()

add_todo('Todo one')
add_todo('Todo two')
add_todo('Todo three')

print(get_all())

"""
3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""

print(' [TASK 3] '.center(70, '-'))


def expanded_form(num: int) -> str:
    num_str: str = str(num)
    num_last: int = len(num_str) - 1
    # res: list[str] = [str(int(v) * (10 ** (num_last - k))) for k, v in enumerate(num_str) if v != '0']
    res: list[str] = [v + '0' * (num_last - k) for k, v in enumerate(num_str) if v != '0']
    return ' + '.join(res)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

"""
4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована 
цим декоратором, та буде виводити це значення після виконання функцій

@decor
def func1():
    print('func1')
    
@decor
def func2():
    print('func2')
    
func1()
func1()
func2()
func1()
    
.........................

count: 1
func1
--------------------
count: 2
func1
--------------------
count: 1
func2
--------------------
count: 3
func1
--------------------
    
    
"""

print(' [TASK 4] '.center(70, '-'))


def decor(func: Callable) -> Callable:
    counter: int = 0

    def inner(*args, **kwargs) -> Any:
        nonlocal counter
        counter += 1
        print(f'count: {counter}')
        res = func(*args, **kwargs)
        print('-' * 20)
        return res

    return inner


@decor
def func1() -> None:
    print('func1')


@decor
def func2() -> None:
    print('func2')


func1()
func1()
func2()
func1()
