#Python5

## 5. I/O模块

### 5.1 文件读写

- Python自带的文件读写函数和C语言兼容
- `with`关键词可以简写`try finally close`等关键词
- `read`方法有很多用法，注意这些用法两次之间是有“记忆”的，即第二次`read`会接着上次继续读
- `write`方法可以用来写文件
- 读写文件的可选参数包括`encoding,mode`
- 除了文件`file`之外，许多类似的对象有着一样的处理方法，例如`StringIO,ByteIO`

### 5.2 文件操作

- `os`模块可以方便的使用操作系统开设的接口
- `os.path.join()`函数可以在不同的操作系统下拼接目录名和文件名
- `os.path.split()`函数可以在不同的操作系统下拆分目录名和文件名

### 5.3 序列化和反序列化

- `pickle`模块可以序列化和反序列化Python对象为二进制文件
- `json`模块可以序列化和反序列化Python对象为json对象
- `json.dump`方法没有默认的办法序列化class对象，这时需要使用`json.dumps(s, default=lambda obj: obj.__dict__)`

