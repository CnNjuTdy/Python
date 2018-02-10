#Python4

## 4. 面向对象编程特性

### 4.1 类和实例

- 动态的类和实例
- 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


import object_oriented.Student

Student = object_oriented.Student.Student

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
bart.age = 8#bart有属性age，但是lisa没有
```

### 4.2 访问限制

- 双下划线开头的变量（非双下划线结尾）的变量语法上规定为外部不可见变量，即私有变量（其实也不是完全不能访问，因为python解释的时候会把这个变量改名字，实际上还是可见的）
- 单下划线开头的变量语法上可见，但语义上表明作者并不想外部直接使用这个变量
- 双线划线开头和结尾的变量是特殊变量，对于外部是可见的，不要命名这样的变量
- python在语法上没有访问限制，一切全靠自觉

### 4.3 继承与多态

- 作为动态语言，不需要严格的类型匹配，只需要有对应的方法
- 允许多重继承
- `isinstance(instance,*)`方法可以检测某个变量是否是某个类型

### 4.4 对象信息

- `type()`函数返回`class`对象，可以用模块`types`里面的常量进行比较
- `isinstance(instance,*)`方法可以检测某个变量是否是某个类型，或某几种类型其中一种
- `dir()`方法可以获得某个变量的所有方法
- `getattr(),setattr(),hasattr()`，其中get方法可能会抛出错误，可以设置默认值

一个好的实践

```python
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

### 4.5 实例属性和类属性

- 相当于静态变量和成员变量，同名实例属性会屏蔽类属性
- 可以删除实例属性使类属性显示出来

### 4.6 限定其自由度

- `__slots__`变量可以限定一个类的实例可以动态添加哪些属性（使用`tuple`）
- 注意这个方法没有办法限定类属性

### 4.7 @property

- 类似于Java的lombok，但是好用很多
- 通过给属性添加`@property`和`@attr_name.setter`，可以实现get和set方法，但是不用写明`getXXX`或者`setXXX`,还是一样的调用，但是效果已经有了

```python
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if value[:1] == 'a':
            return
        else:
            self._name = value
   
bart = Student('Bart Simpson', 59)
bart.name = 'aaaa'#相当于调用name(value)
print(bart.name)#相当于调用name(),修改失败了
bart.name = 'Smith'
print(bart.name)#修改成功
```

### 4.8 定制类

实质上，所有的对象都有一些特殊属性，可以用来定制类

```python
#__str__和__repr__类似toString方法
def __str__(self):
    return '%s: %s' % (self._name, self._score)

__repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
	
    #__iter__和__next__方法实现了之后可以用于for in循环
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  
            raise StopIteration()
        return self.a 
	#__getitem__用于使用a[]语法，当然实现起来很麻烦，因为这个语法里面可以切片
    def __getitem__(self, n):
           a, b = 1, 1
           for x in range(n):
               a, b = b, a + b
           return a
    #__getattr可以获得某个属性，这里可以返回函数
    def __getattr__(self,value):
        pass
    #__call__可以使得对象名()来调用
    def __call__(self):
        print('My name is %s.' % self.name)
```

### 4.9 枚举类

- 注意普通枚举类对应的value从1开始

```python
from enum import Enum

#普通枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#精确枚举类
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

### 4.10 错误定义和处理

- 主要关键词`try,exception as,finally,rasie`类似`try,catch,finally,throw`
- 错误没有捕获的时候，会在异常栈向上抛出，如果一直没有抛出，会导致系统停止运行
- 其他和Java一样
