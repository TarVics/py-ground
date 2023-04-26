import math
import time
import multiprocessing


def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


def work(num):
    return str(math.sqrt(math.sqrt(math.sqrt(num / 2) * 10 / 15))) + 'H'


@time_decor
def main_process():
    print('main')
    r = range(10000000)
    with open('file1.txt', 'w') as file:
        for num in r:
            res = work(num)
            print(res, file=file)


# main_process()
@time_decor
def mp():
    print('mp')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')
    with multiprocessing.Pool(count) as p:
        r = range(10000000)
        with open('file2.txt', 'w') as file:
            tasks = p.map(work, r)
            for task in tasks:
                print(task, file=file)


if __name__ == '__main__':
    mp()
