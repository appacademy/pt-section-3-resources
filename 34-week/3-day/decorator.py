# Decorators in Python

# 1. Functions are first-class objects in Python.
# This means they can be passed around and used as arguments.



# def greet(name):
#     return f"Alright, welcome in, let's wait until {name} rolls in."

# def wrap_greet(func, name):
#     return func(name)

# print(wrap_greet(greet, "Will"))
# print()





# 2. Python supports higher-order functions.
# These are functions that take other functions as arguments and/or return functions.
def func_y():
    print("this is funcy")

def my_func(some_func):
    def my_random_inner_func():
        print("Cool")
        some_func()
    return my_random_inner_func

# print("funcy", func_y)
# print("my func", my_func)


# return_answer = my_func(func_y)
# print(return_answer)
# return_answer()

@my_func
def func_y():
    print("this is funcy")

func_y()

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# def ordinary():
#     print("I am ordinary")

# Decorating `ordinary` manually without `@`
# pretty = make_pretty(ordinary)
# pretty()
# print()


# 3. Using the @ symbol for decorators.
# The @ symbol offers a shorthand to decorate a function.


# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary again")

# ordinary()


# 4. A more detailed example of a decorator
# This decorator prints statements before and after the decorated function is executed.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()



# @is_user_authenticated
# def my_route():
#     print("Hello!")

# say_hello()

# # 5. Decorators that can accept arguments.
# # This allows us to decorate functions that accept arguments.

# def my_decorator_with_args(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#     return wrapper

# def my_decorator_with_args_custom(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called. COOL")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called. COOL")
#     return wrapper

# @my_decorator_with_args
# @my_decorator_with_args_custom
# def custom_greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# # @my_decorator_with_args_custom
# # def say_hello():
# #     print("Hello! WORLD")

# custom_greet("Bob", greeting="Good morning")

# # say_hello()
