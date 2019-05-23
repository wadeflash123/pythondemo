# 函数式编程 functional programming

# 高阶函数（high-order function）
  # 1.变量可以指向函数
  # 2.函数名也是变量
  # 3.传入函数

# 编写高阶函数，就是让函数的参数能接收别的函数

# map/reduce
# reduce 把上次计算结果和下一个元素传入 function 继续运算

def f(x):
  return x * x

m1 = map(f, [1, 2, 3])
print(m1, list(m1))

def sum1(x, y):
  return x + y

from functools import reduce
r1 = reduce(sum1, [1, 2, 3])
print(r1)

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# ascii 码
def normalizeName(name):
  print(name[0], name[1:])
  return name.capitalize()
names = map(normalizeName, ['adam', 'LISA', 'barT'])
print(list(names))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
  pass

# print(str2float('123.456'))


# filter
def is_odd(x):
  return x % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# 用 filter 求素数

# sorted 排序函数，key 函数，reverse


# 返回函数：函数作为返回值/闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

# 匿名函数：当我们在传入函数时，有时直接传入匿名函数更方便
lambda x: x * x # 只能有一个表达式，不用写 return，返回值就是该表达式的结果

# 等价于：
def f2(x):
  return x * x

# 可以把匿名函数赋值给一个变量，也可以把匿名函数作为返回值