# Python6

## 6. 正则表达式

- Python内建了正则表达式re模块
- 匹配：`re.match(regRex,str)`
- 拆分：`re.split(regRex,str)`
- 分组：`re.match(regRex,str).group(num)`

## 7. 常用内建模块

### 7.1 datetime

- 写好了的`dateutil`
- 但是注意`datetime`是一个模块，里面有个类叫做`datetime`类，需要使用dateutil类的时候要用`from datetime import datetime`
- 使用`datetime`模块的`timedelta`可以直接加减时间

### 7.2 哈希算法

- 写好了的`md5util`
- 为了应付黑客，可以把用户的密码用哈希算法加密之后存入数据库
- 为了防止黑客进行惯用破解，可以在用户密码之后添加字符串再进行加密
- 该字符串可以和用户名挂钩等等

### 7.3 迭代器工具

- `itertool`提供了一系列算法，可以生成迭代器
- `count(n)`生成从n开始的自然数迭代器
- `cycle(sequence)`无限循环传入的序列
- `repeat(obj,num)`循环obj，次数为num
- `chain(iter,iter)`串联两个迭代器

### 7.4 url工具

- `urllib`模块提供了访问http资源的方式
- 主要应用的类包括`request,parse`

```python
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
```