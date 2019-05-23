# 装饰器 decorator：就是返回函数的高阶函数

import functools

# 定义一个打印日志的 decorator：
def log(func):
  @functools.wraps(func)
  def wrapper(*args, **kw): # 定义参数 (*args, **kw)，则 wrapper 可以接受任意参数
    print('call %s()' % func.__name__)
    return func(*args, **kw)
  return wrapper

def log2(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
      print('%s %s():' % (text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator

@log2('today')
def now():
  print('2019-05-16')

now()

# 偏函数：partial func
print(int('12345', 16)) # 可以支持把其他进制转成十进制
def int2(s, base=2):
  return int(s, base)

# functools.partial：当函数的参数个数太多，需要简化时，
#   使用 functools.partial 可以创建一个新的函数，这个新函数可以“固定住”原函数的部分参数，从而在调用时更简单
# 相当于新函数有新的默认值