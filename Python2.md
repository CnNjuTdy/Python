#Python2

## 2. 语法特性

###2.1 list和tuple

- list类似于Java中的java.util.List，更好用，并且可以用负index来从后往前访问

- tuple应该是一个对象概念，一旦被初始化就不能改变，但是如果初始化的元素是个指针，其指向的内容可以改变（常指针）

  list，tuple和str都可以用`+`直接连接

### 2.2 语句书写

书写习惯和命名规范和C语言类似

与Java C JavaScript有很大不同，大体上，冒号代替了前大括号的作用，而后大括号的终止效果则由缩进表示

```python
if a > 18:
    print("hello ,adult")
elif a > 3:
    print("hello ,child")
else:
    print("hello ,baby")

x = ["Tang Daye", "Zhou Yaqing"]
for name in x:
    print("hello, " + name)
    
sum2 = 0
for x in range(101):
    sum2 = sum2 + x
print(sum2)

sum2 = 0
n = 100
while n > 0:
    sum2 = sum2 + n
    n = n - 1
print(sum2)
```

### 2.3 标准输入输出

- print函数综合了Java和C的特点，input函数只会返回字符串变量
- Python3中字符串和数字不能直接加（没有自动类型转换），要用函数`str(number)`

```python
print("%.2f" % 3.1415926)
print("hello "+"world")
x = input("x = ") #输入3时a='3'
```

### 2.4 dic和set

字典，Java中的map和JavaScript中的对象，键值对存储形式，写法和JavaScript一样，取存方式和Java一样（也可以用JavaScript类似的直接取存但是不推荐）。为保证hash函数返回值的唯一性，dic的key值必须是不可变对象，dic使用空间换取时间。

```python
x = {
    "Tang": 100,
    "Zhou": 99
}
print(x.get('Zhou'))
```

集合，Java中的Set，不可重复的组合，有交并运算

```Python
x = {
    "Tang": 100,
    "Zhou": 99
}
y = set(x)
print(y)
```

### 2.5 定义函数

- 不使用function等关键词（JavaScript，PHP），也没有返回值声明（C，Java）。
- 当函数暂且不做事情时，可以用`pass`关键字（由于python中空代码块是非法的，必须要有东西代替）。
- 函数可以返回多个值(以tuple形式返回，省略小括号)，这很好用（可以写函数来计算方程的多个解了）
- 函数的参数都是形参，当然如果传入的值是字典或者列表是可以被改变内容的

```python
def area_of_circle(r):
    return cmath.pi*r*r


def func(x, y):
    return x + 1, y + 1


a, b = func(2, 3)
```

### 2.6 模块

Java和C的库概念，可以自己编写

例如将2.5中的`area_of_circle`写在了my_lib.py中，my_lib可以看成一个模块，通过指令`import my_lib`，可以使用该函数`my_lib.area_of_circle(3)`

`import`关键词会执行原有的文件里可以执行的语句（非函数部分），这和JavaScript是一样的

```python
import lib.newTest
foo = lib.newTest.area_of_circle
print(foo(2))
```

### 2.7 函数参数

- 和Cpp类似的默认参数定义（必须要是不变的对象，因为某个函数的默认参数在定义指出会被初始化，如果发生变化会引起误解）
- 很独特的按照名字注入参数，这有一些像SpringMVC在处理http参数的时候的做法，但是Java需要注解，这里不需要
- Java类似的可变参数定义，这里接受的可变参数将会是一个tuple
- 很独特的关键字参数定义，这里接受的可变参数将会组装成dic
- 参数组合：在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

> 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

```python
#默认参数定义和按照名字注入参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll("LiLei", "M")
enroll("HanMeimei", "F", city="Tianjin")


#可变参数定义
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2,3)
calc(*[1,2,3])

#关键字参数定义
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer')
ext = {'gender':'M', 'job':'Engineer'}
person('Adam', 45, **ext)
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

### 2.8 尾递归优化

尾递归：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式

python和其他很多编程语言一样，没有对尾递归进行优化，因此即使人为编写尾递归代码，该栈溢出的还是会栈溢出

```python
#递归方式解决汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a + "-->" + c)
    else:
        move(n - 1, a, c, b)
        print(a + "-->" + c)
        move(n - 1, b, a, c)
```

### 2.9 切片

- 类似于Java的subString（含头不含尾），但是好用很多很多很多，不得不说python对于list的支持真的强大
- 可以用负数切片
- 字符串和tuple都可以切片
- 切片中遇到前一个数比后一个数大时，如果这两个数符号相同，会直接返回空list（空串，空tuple），否则会先转成符号相同的（`list[1:-1]`会返回不包含头尾的list）
- 切片中遇到超出上下限的情况时，会保留有意义的部分，忽略没有意义的部分
- 切片可以用来赋值
- 切片可以指定步长。`list[::-1]`会返回这个序列的逆序

```python
x = [2,3,4,100,2]
y = x[2:4]
z = x[:4]
w = x[-2:]
#y=[4,100]
#z=[2,3,4,100],省略0
#w=[100,2],后两个元素，省略0

x=(2,3)
y=x[4,1]
#y=()

x = (2,3)
y = x[:4]
#y=(2,3)
```

### 2.10 迭代器

- 类似于Java`for :`循环和JavaScript的`for in`循环，但是好用很多（和JavaScript有点像）
- list，tuple，str，dic，set都可以用迭代器循环

```python
x = {"Tang":99,"Zhou":90,"Wan":90}
for value in x.values():
    print(value)
for key,value in x.items():
    print(str(key)+": "+str(value))
```

### 2.11 列表生成式

1. 连续的正数列表可以用`list(range())来生成`
2. 可以很自由的生成具有其他特征的列表（类比Excel的自动填充）,或者快速由一个或多个可迭代对象生成另一个列表

```python
#靠近前面的先执行
list = ['Hello', 'World', 'IBM', 'Apple']
s = [y+y for x in list for y in x]
#先循环x
y = [1, 2, 3, 4, 5, 6]
x = [2, 7, 3, 4, 5, 6]
z = [str(i) + str(j) for i in x for j in y]
print(z)
#['21', '22', '23', '24', '25', '26', '71', '72', '73', '74', '75', '76', '31', '32', '33', '34', '35', '36', '41', '42', '43', '44', '45', '46', '51', '52', '53', '54', '55', '56', '61', '62', '63', '64', '65', '66']
```

###2.12 生成器

- 和之前学的有很大不同……看起来有点复杂
- 简单说，生成器函数就是讲列表生成式的`[]`换成`()`，得到的不再是个列表（但是仍然可以迭代）,而是一个生成器对象，它每次迭代或者取值的时候需要进行计算，也会越界
- 如果在函数定义中包含了关键字`yield`，那么整个函数的将会是一个迭代器，在直接调用时不会执行，而是在调用方法`next()`时执行，执行到`yield`关键字为止，并把`yield`关键字后的值作为该次生成器的返回值，换句话说，这个函数中`yield`关键词的个数就是生成器长度（也可能是无穷长的）。
- **注意不要试图去list一个无限长的生成器**
- 可以用于`for`循环的对象称为可迭代对象`Iterable`，可以用`next`方法的称为迭代器`Iterator`，`Iterable` 真包含`Iterator`。`Iterator`是一个数据流的概念，可以表示无限大的数据流，`Iterator`的计算是惰性的

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1


import lib.newTest

foo = lib.newTest.fib
x = foo(6)
print(x)
#generator
print(list(x))
#[0,1,1,2,3,5]

#杨辉三角1
def triangles():
    my_list = [1]
    while True:
        yield my_list
        my_list = [1] + [my_list[i] + my_list[i + 1] for i in range(len(my_list) - 1)] + [1]
#杨辉三角2      
def triangles():
    my_list = [1]
    while True:
        yield my_list
        my_list.append(0)
        my_list = [my_list[i - 1] + my_list[i] for i in range(len(my_list))]
```
