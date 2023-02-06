import inspect


def print_caller():
    stack = inspect.stack()
    the_caller = stack[1]
    print("Caller:", the_caller[3])
