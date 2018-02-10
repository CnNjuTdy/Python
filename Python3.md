#Python3

## 3. 函数式编程特性

### 3.1 函数作为第一等公民 

- 函数和其他受类型一样，可以被赋予给一个变量，也可以作为另一个函数的入参和返回值
- 和JavaScript类似

### 3.2 匿名函数

- 关键词`lambda`可以定义匿名函数，类似于JavaScript
- 回归了函数的本质，即映射`lambda x:y`映射x为y
- 缺点：只能有一个表达式，不能做比较复杂的操作，不能写return和其他控制块
- 优点：不用担心命名冲突，可以被赋值，可以返回，十分简洁明了

### 3.3 高阶函数

- 数学意义上的复合函数，即把一个函数作为另一个函数的入参

- 和JavaScript类似

  ```python
  def my_func(operate, *nums):
      return operate(*nums)
  def add_func(*nums):
      result = 0
      for num in nums:
      	result = result + num
      return result

  print(my_func(add_func, 1, 2, 3, 4))
  ```


  #### 3.3.1 map/reduce

- Python内建了映射和规约函数
- `map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回
- `reduce()`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算

```python
def normalize_single(name):
    return name[:1].upper() + name[1:].lower()


def normalize(names):
    return list(map(normalize_single, names))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}



def char2num(s):
    return DIGITS[s]


def str2int(s):
    return functools.reduce(lambda x, y: x * 10 + y, map(char2num, s))
```

  #### 3.3.2 filter

- 和`map`函数类似，接受一个函数和一个序列，不同的是，这个`filter`函数根据传入函数的返回值是`True`和`False`来决定是否保留某个元素


```python
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
    pass
```

  ####3.2.3 sorted

- 内建的高阶函数`sorted`，其命名参数`key`规定一种映射，将列表中的各项映射到可以比较元素（最基本的就是数字和字符串），然后进行比较。命名参数`reverse`规定是否反序

```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda x: x[0]))#姓名从低到高
print(sorted(L, key=lambda x: x[1], reverse=True))#成绩从高到低

```

### 3.4 函数作为返回值

- 函数可以作为返回值返回，并在后续中调用
- 注意函数作为返回值返回时并没有调用，所以在该函数中不要使用后续发生变化的变量

### 3.5 装饰器

- Python内建了装饰器模式，其实质是将一个函数加以包装，返回另一个函数

```python
def log(func):
    def wrapper2(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper2


#调用下面函数的时候,会打印调用信息，但是这其实是不正确的，应为返回的函数发生了变化，变成了
#<function log.<locals>.wrapper2 at 0x10c1de400>
@log
def primes():
    yield 2
    nums = odd_num_larger_than_2()
    while True:
        n = next(nums)
        yield n
        nums = filter(lambda x: x % n > 0, nums)
        

#这样的调用结果是正确的
#@functools.wraps(func)
def log(func):
    @functools.wraps(func)
    def wrapper2(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper2
```
###3.6 偏函数 

- 当参数过多需要简化时，可以用偏函数来新建一个函数。这个新函数可以固定住原函数的部分参数，从而在调用时更简单

```python
max2 = functools.partial(max, 10)
```