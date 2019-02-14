#创建案例
#创建Student类，描述学生类
#学生具有Student.name属性
#但name格式并不统一
#可以增加一个函数，

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #介绍自己
    def intro(self):
        print("hi,my name is {0}".format(self.name))

    def setname(self):
        self.name = name.super()

s1 = Student("zqc",20)
s1.intro()

#property案例
# 定义一个person类，具有name，age属性
#对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，用整数保存
# x=property(fget,fset,fdel,doc)
class Person():
    def fget(self):
        return self._name * 2

    def fset(self,name):
        self._name = "NOName"

    def fdel(self):
        self._name = "NoName"
    name = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
p1.name = "zqc"