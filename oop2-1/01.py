'''
定义一个学生类，用来形容学生
'''
#定义一个空的类
class Student():
        pass

# 定义一个对象
mingyue = Student()

#定义一个类，用来描述听python的学生
class PythonStudent():
    name = None
    age = 18
    course = "python"
    #需要注意
    #1.def doHomework的缩进层级
    #2.系统默认由一个self参数
    def doHomework(self):
        print("我在做作业")

        #推荐在函数末尾使用return语句
        return None
yueyue = PythonStudent()
yueyue.name = yueyue
print("123")
yueyue.doHomework()

