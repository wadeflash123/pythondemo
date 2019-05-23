# list 特性
# -1, -2,...
# list 是一个可变的有序表
# 方法：append, insert, pop
fruits = ['apple', 'banana']
print(fruits)
fruits.append('orange')
print(fruits)
fruits.insert(1, 'lemon')
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

# tuple 特性
# tuple 不可变
# 定义只有一个元素 tuple (2,)
t = (1,)
print(t)
tt = (1, 2, [3, 5])
tt[2][1] = 6
print(tt)