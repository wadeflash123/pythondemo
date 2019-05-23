#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '

__author__ = 'Jay'

# 以上是Python模块的标准文件模板

import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('Hello world %s' % args[0])
  elif len(args) == 2:
    print('Hello %s!' % args[1])
  else:
    print('too many arguments')

if __name__ == '__main__':
  test()

# 命令行导入 use_modules 模块：在命令行里输入 import use_modules，然后调用 use_modules.test()

### 作用域
# 正常的函数和变量名是公开的(public)，比如 a, PI
# __xxx__ 这种形式为特殊变量，有特殊用途，自己定义的变量不要使用这种形式
# _xxx 或 __xxx 这种形式的函数和变量是私有的(private)，不应该被直接引用
#   python 并没有一种方法可以完全限制访问访问 private 函数或变量，但是从编程习惯上不应该引用私有变量


### 安装第三方模块
# 包管理工具 pip exp：pip install Pillow

### 模块搜索路径

# import 模块时，Python 会搜索当前目录、所有以安装的内置模块和第三方模块，搜索路径放在 sys 模块的 path 变量中
print(sys.path)

# 添加额外的搜索路径：
# 1.修改 sys.path：sys.path.append('/mypath/to/my_modules') 这种方式在运行时修改，运行后失效
# 2.设置一个新的环境变量：PYTHONPATH，这个环境变量的值会被添加到搜索路径中
