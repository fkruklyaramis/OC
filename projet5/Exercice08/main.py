def log_decorator(func):
    def wrapper():
        print("Start function, do something...")
        func()
        print("End function")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
