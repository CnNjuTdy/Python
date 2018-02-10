import math
import functools
import time
import inspect

import itertools

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def metric(arg):
    if inspect.isfunction(arg):
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            time.clock()
            ret = arg(*args, **kw)
            print('Tip: default')
            print('%s executed in %s ms' % (func.__name__, round(time.clock() * 1000)))
            return ret

        return wrapper

    else:
        def decorator(func):

            @functools.wraps(func)
            def wrapper(*args, **kw):
                time.clock()
                ret = func(*args, **kw)
                print('Tip: %s' % arg)
                print('%s executed in %s ms' % (func.__name__, round(time.clock() * 1000)))
                return ret

            return wrapper

    return decorator


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return functools.reduce(lambda x, y: x * 10 + y, map(char2num, s))


def area_of_circle(r):
    return math.pi * r * r


def func(x, y):
    return x + 1, y + 1


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def move(n, a, b, c):
    if n == 1:
        print(a + "-->" + c)
    else:
        move(n - 1, a, c, b)
        print(a + "-->" + c)
        move(n - 1, b, a, c)


def my_trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


def my_lower(list):
    return [s.lower() for s in list if isinstance(s, str)]


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1


def triangles():
    my_list = [1]
    while True:
        yield my_list
        my_list.append(0)
        my_list = [my_list[i - 1] + my_list[i] for i in range(len(my_list))]


def my_func(operate, *nums):
    return operate(*nums)


def product(num1, num2):
    return num1 * num2


def prod(nums):
    return functools.reduce(product, nums)


def normalize_single(name):
    return name[:1].upper() + name[1:].lower()


def normalize(names):
    return list(map(normalize_single, names))


@metric("123")
def str2float(str):
    s1, s2 = str.split(".")
    return str2int(s1) + str2int(s2) / 10 ** len(s2)


def odd_num_larger_than_2():
    t = 1
    while True:
        t = t + 2
        yield t


def primes():
    yield 2
    nums = odd_num_larger_than_2()
    while True:
        n = next(nums)
        yield n
        nums = filter(lambda x: x % n > 0, nums)


def is_palindrome(nums):
    return filter(lambda n: int(str(n)[::-1]) == n, nums)


def get_pi(n):
    # return sum([(4 if x % 2 == 0 else -4) / (2 * x + 1) for x in range(n)])
    c = itertools.cycle([4, -4])
    t = itertools.count(1, 2)
    return sum(next(c) / next(t) for x in range(n))