from time import time

def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        t = f"{(t2-t1):.7f}"
        print(f'Function {func.__name__!r} executed in {t}s')
        return result
    return wrap_func