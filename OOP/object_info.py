
# 获取对象信息
# typeof()
print(type(123), type(abs))

import types
def fn():
  pass

print(type(fn) == types.FunctionType, type(lambda x: x) == types.LambdaType)

# isinstance()
# isinstance 可以用于判断 class 类型
# 能用 type() 判断的基本类型也可以用 isinstance() 判断

# 并且还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))

# dir()
# 如果要获得一个对象的所有属性和方法，可以使用 dir() 函数，返回一个包含字符串的 list：
# print(dir('abc'))


# 实例属性和类属性
# 实例属性
class Student(object):
  def __init__(self, name):
    self.name = name

s = Student('Bob')
s.score = 99

# 类属性
class Student2(object):
  clazzname= 'Student2'

s2 = Student2()
print(s2.clazzname)
