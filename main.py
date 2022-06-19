import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        time_spent = end - start
        print(f'Total time used to run {func.__name__} is {time_spent:.4f} secs ')
        return value
    return wrapper

@timer
def do_something(num):
    for i in range(num):
        sum([i*2 for i in range(num)])


do_something(1000)