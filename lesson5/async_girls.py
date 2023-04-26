import asyncio
import time
import httpx
from uuid import uuid1


# import requests
#

def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


# def get_res(url):
#     return requests.get(url, allow_redirects=True)
#
# def write_file(res: requests.Response):
#     filename = f'{uuid1()}.jpg'
#     with open(filename, 'wb') as file:
#         file.write(res.content)
#
# @time_decor
# def main():
#     url = 'https://loremflickr.com/g/320/240/girl'
#     for _ in range(50):
#         write_file(get_res(url))
#
#
# main()


def write_file(data):
    file_name = f'{uuid1()}.jpg'
    with open(file_name, 'wb') as file:
        file.write(data)


async def get_res(url, client):
    res = await client.get(url, follow_redirects=True)
    write_file(res.read())


async def start():
    url = 'https://loremflickr.com/g/320/240/girl'
    tasks = []
    async with httpx.AsyncClient() as client:
        for _ in range(50):
            task = asyncio.create_task(get_res(url, client))
            tasks.append(task)
        await asyncio.gather(*tasks)


@time_decor
def main():
    asyncio.run(start())


main()
