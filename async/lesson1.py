# async programming 

import time
import asyncio 


# def hello():
#     print('Hello')
#     time.sleep(2)
#     print('World')


# hello()

# _______________________ _______________________ _______________________ _______________________


# async def hello():
#     print('Hello')
#     await asyncio.sleep(2)
#     print('World')


# asyncio.run(hello())

# _______________________

# def say(message, delay):
#     time.sleep(delay)
#     print(message)

# def main():
#     say("Hello", 2)
#     say("World", 1)
#     say("Python", 3)

# main()

# async def name():
#     print('Hello')
#     await asyncio.sleep(2)
#     print("World")
# async def hello():
#     print('Hello')
#     await asyncio.sleep(1)
#     await name()
#     print("World")
    
# asyncio.run(hello())



# def name():
#     print('Hello')
#     time.sleep(5)
#     print("World")
# def hello():
#     print('Hello')
#     time.sleep(2)
#     print("World")
#     name()

# hello()


import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2



import datetime
now = datetime.datetime.now()

asyncio.run(main())

end = datetime.datetime.now()
print(end-now)
