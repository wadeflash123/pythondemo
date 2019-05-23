# dict 字典集合
# in 判断 key 是否存在
# 方法：get -- 获取 value, key 不存在返回 None; pop -- 删除 key
# 特点：查找和插入的速度极快，不会随着 key 的增加而变慢
#       需要占用大量的内存
# 相反：list 特点：查找和插入的时间随着元素的增加而增加
#       占用空间相对小
d1 = {
  1: [1, 2],
  2: (1,),
  (6,): 666
}
print(d1, d1.get(3, -1))
# set 一组 key 的集合，但不存储 value. key 不会重复
# set 无序，初始化传入 list，重复元素会被自动过滤
# 方法 add(key), remove(key)
# * set 可以看成数学意义上的无序和无重复元素的集合，因此两个 set 可以做交集、并集等操作

s1 = set([1, 2, 3])
print(s1)
s2 = set([2, 5, 6])
print(s1 & s2)
print(s1 | s2)
# s3 = set([1, 2, [2]]) # unhashable type: 'list'
s4 = set([1, 0, (5,)])
print(s4)
