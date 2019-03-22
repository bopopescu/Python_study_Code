# 包含一个学生类
# 一个sayHello函数
# 一个打印语句
'''
class Student():
    def __init__(self,name = "NoName",age=18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0}".format(self.name))
def sayHello():
    print("这是例子one")

# 此判断语句建议一直作为程序的入口
if __name__ == "__main__":
    print("我是模块one啊！")
'''
#=========================================
# 查看所有模块的搜索路径
import sys
print(type(sys.path))
print(sys.path)
