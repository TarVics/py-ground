import threading
import time

# def show(n):
#     for i in range(n):
#         time.sleep(0.5)
#         print(i, threading.current_thread().name)
#
#
# thread1 = threading.Thread(target=show, args=(5,), name='th-1')
# thread2 = threading.Thread(target=show, args=(8,), name='th-2')
#
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# show(2)

cont = 0
lock = threading.Lock()


def inc():
    with lock:
        global cont
        cont += 1
        print(cont)


threads = []
for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for item in threads:
    item.join()
