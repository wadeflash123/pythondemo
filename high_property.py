# 高级特性 

###### ------ 切片 slice
# list, tuple, str 的切片操作 [i:j:step] i j 可以为空值或负整数正整数0, step 表示步长
# 利用切片，实现一个字符串 trim 函数
def trim(str):
  while str[:1] == ' ':
    str = str[1:]
  while str[-1:] == ' ':
    str = str[:-1]
  return str
print(trim('                  hello trim '))


###### ------ 迭代
# list, tuple for x in lt
# dict for k in dt, for v in dt.values(), for k, v in dt.items()
# 判断一个对象是否可迭代 -- 通过 collections 模块的 Iterable 判断
from collections import Iterable, Iterator
print(isinstance('ABC', Iterable))
# enumerate 可以把一个 list 变成 索引-元素 对
for i, item in enumerate(['a', 'b', 'c']):
  print(i, item)
for x, y in [(1, 1), (2, 3), (5, 8)]:
  print(x, y)


###### ------ 列表生成器
print([x * x for x in range(1, 11)])
# 两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])
import os
print([d for d in os.listdir('.')]) # 打印当前目录下的所有子目录和文件名

L1 = ['Hello', 'world', 19, 'Apple', None]
L2 = [v for v in L1]
L3 = []

for v in L1:
  if isinstance(v, str):
    L3.append(v.lower())

print(L3)


###### ------ 生成器 generator
G1 = (x for x in range(10)) # 定义了一个 generator 方式一
print(G1, next(G1), next(G1))
for n in G1:
  print(n)

# 定义 generator 方式二 yield 关键字

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b # print(b)
    a, b = b, a + b
    n = n + 1
  return 'done'

print(fib(9), next(fib(9))) # fib(9)

f = fib(8)
print(next(f), next(f))
for b in f:
  print(b)

# generator 函数：generator 函数和普通函数执行顺序不一样。普通函数是顺序执行，遇到 return 语句或者
#                 最后一行语句就返回；而 generator 函数在每次调用 next() 的时候执行，遇到 yield
#                 语句返回，再次执行时从上次返回的 yield 语句出继续执行。                

# 打印杨辉三角每一行数据 list
def triangles():
  pass


###### ------ 迭代器 iterator

# 可迭代对象 Iterable：可以直接作用于 for 循环的对象统称为可迭代对象
# 一种是集合数据类型比如：list\tuple\dict\set\str
# 一种是 generator，包括生成器和带 yield 的 generator function

print(isinstance([], Iterable)) # True

# 迭代器 Iterator：可以被 next() 函数调用并不断返回下一个值的对象称为迭代器

# print(isinstance((x for x in range(10)), Iterator))

print(isinstance((x for x in range(10)), Iterator)) # True
print(isinstance('abc', Iterator)) # False

# 生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterable，却不是 Iterator；
# 把 list、dict、str 等Iterable变成Iterator可以使用 iter() 函数
print(isinstance(iter('abc'), Iterator)) # True

# Iterator 迭代器表示的是一个惰性计算的数据流（序列），不能提前知道其序列长度，只能通过 next 函数
#   不断获取下一个数据，直到没有数据时抛出 StopIteration 错误。

# Iterator 甚至可以表示一个无限大的数据流，例如全体自然数；而使用 list 是永远不可能存储全体自然数的。
# Python 的 for 循环本质上就是通过不断调用 next() 函数实现的：
for x in [1, 2, 3, 4, 5]:
    pass
# 等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
  try:
    # 获得下一个值:
    x = next(it)
  except StopIteration:
    # 遇到StopIteration就退出循环
    break
