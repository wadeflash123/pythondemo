# 面向对象编程把对象作为程序的基本单元，一个对象包含数据和操作数据的函数
# 计算机程序的执行就是一系列消息在各个对象之间传递
# 接受消息、处理消息、发送消息
# 封装、继承、多态

# class Student():
#   pass

# jay = Student()

# print(jay, Student)

class Teacher():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def print_info(self):
    print('%s: %s' % (self.name, self.age))

  def get_grade(self):
    if self.age > 60:
      return 'retired'
    elif self.age > 40:
      return 'high level'
    else:
      return 'middle level'

Q = Teacher('xiao q', 25)

print(Q, Q.name)

Q.print_info()

print(Q.get_grade())

Q.sex = 'female' # 对象额外添加的属性

print(Q.sex)

# 访问限制
# 私有变量： __ 起始命名：__name，只有内部可以访问 (实际上姓名变量名称由解析器改成了 _Student__name)

class Student():
  def __init__(self, name, score):
    self.__name = name
    self.__score = score
  
  def print_score(self):
    print('%s\'s score: %s' % (self.__name, self.__score))

  # 增加 getter 方法
  def get_name(self):
    return self.__name
  
  # 增加 setter 方法
  def set_score(self, score):
    self.__score = score

wade = Student('wade', 66)

wade.print_score()
# print(wade.__score) # 不可访问、不可修改
print(wade.get_name())
wade.set_score(88)
wade.print_score()


### 继承和多态
class Animal(object):
  def run(self):
    print('animal is running ...')

class Dog(Animal):
  # pass
  def run(self):
    print('dog is running ...')

husky = Dog()

husky.run()

def run_twice(ani):
  ani.run()

run_twice(husky)
  
# 静态语言(Java) vs 动态语言(Python) 动态语言的鸭子类型特点
