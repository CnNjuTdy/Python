class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

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

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            return
        if value > 100 or value < 0:
            return
        else:
            self._score = value

    def __str__(self):
        return '%s: %s' % (self._name, self._score)

    __repr__ = __str__


class Screen(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            return
        else:
            if value < 0:
                return
            else:
                self._width = value
                return

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            return
        else:
            if value < 0:
                return
            else:
                self._height = value
                return

    @property
    def resolution(self):
        return self._width * self._height


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
