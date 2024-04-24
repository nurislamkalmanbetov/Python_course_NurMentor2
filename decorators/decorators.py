# decorators 

# def decorator(func):
#     def wrapper():
#         print("Действие до выполнения функции1")
#         func()
#         print("Действие после выполнения функции2")
#     return wrapper

# @decorator
# def hello():
#     print("Hello world!")

# hello()
# # __________________________ 

# @decorator
# def hello2():
#     print("Hello world!2")

# hello2()

# _________________________________________________________

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args, **kwargs)
        
        return wrapper
    return decorator

@repeat(5)
def hello(name):
    print(f"Hello {name}")

hello('John')