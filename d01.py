# print abs value of an integer
a = 100
if a >= 0:
  print(a)
else:
  print(-a)
print('i\'m "ok"')
print("i'm \"ok\"")
print(r'\\\\n\\t\\')
print(r'''line1
line2\nlinemid
line3''', not 1)
x = 12
x += 12
# print(x + 'str') # unsupported operand type(s) for +: 'int' and 'str'
x = 'abc'
print(x)
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 100000))
print('%3d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s, Gender: %s' % (25, True))
print('growth rate: %d %%' % 9)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))