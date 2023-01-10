# Create a decorator that will check types.
# It should take a function with arguments and
# validate inputs with annotations.

from __future__ import annotations


def check_types(func):
    def wrapper(*args):
        a = func.__annotations__
        a.popitem()
        try:
            for x in list(args):
                for value in list(a.values()):
                    if x.__class__.__name__ == value:
                        return func(*args)
        except TypeError:
            for x in list(args):
                if x.__class__.__name__ != value:
                    index = args.index(x)
                    return (f"TypeError: Argument {list(a.keys())[index]} must be {list(a.values())[index]}, not {x.__class__.__name__}")

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


print(add(1, '2'))

# Write a decorator that will calculate the execution
# time of a function.


def calculate_execution_time(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        function = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time is {float(end - start)} seconds')
        return function

    return wrapper


@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
