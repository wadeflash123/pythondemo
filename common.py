# 通用函数集
def func_a(a):
  pass

def i_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x

def power(x, n=2):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x

def enroll(name, gender, age=6, city='hangzhou'):
  print('stu info: ', name, gender, age, city)

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
  if L is None:
    L = []
  L.append('END')
  return L

# 可变参数：参数个数可变 *arg
def summary(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

# 关键字参数
def person(name, age, **kw):
  print('name:', name, 'age:', age, 'other:', kw)

# 命名关键字参数
def student(name, age, *, city='杭州', job):
  print('name:', name, 'age:', age, 'city:', city, 'job:', job)

# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict