# 包含一个学生类，一个sayhello函数，一个打印语句
class Student():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age
        print("model1 初始化完毕！")

    def say(self):
        print("My name is :{0}".format(self.name))

def sayHello():
    print("Hi, Welcome to CDUT")
print("我是模块001！")