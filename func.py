# 函数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 内置函数
print(hex(678))
# 定义函数：def func_name(args):
def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x
print(my_abs(-6))
from common import func_a, i_abs
func_a(1)
# print(i_abs('a'))

import math

def move(x, y, step, angle=0):
  nx = x + step * math.cos(angle)
  ny = y + step * math.sin(angle)
  return nx, ny # return a tuple
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

from common import enroll

enroll('xiao ming', 'male')

from common import add_end

print(add_end(), add_end()) # ['END'] ['END']

from common import summary

print(summary(*[0, 1, 2, 3]))

from common import person
person('xiaoming', 9)
person('xiaohon', 8, gender='female', city='hangzhou')
extra = {'gender': 'male', 'city': 'shanghai'}
person('xiaojie', 6, **extra)

from common import student
student('哈哈哈', 5, job='student')