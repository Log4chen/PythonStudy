

class User:
    name = None
    age = None
    __weight = None
    # 构造方法，在类初始化时会自动调用
    # 不能有多个 __int__ 方法 ？
    def __init__(self, name=None, age=None, __weight= None):
        self.name = name
        self.age = age
        self.__weight = __weight

    # 类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例(self不是关键字，也可以用其他名字)
    def say(self):
        print(f'my name is {self.name}, age is {self.age}, __weight is {self.__weight}')
        print(self.__class__)
    # 私有方法
    def __sleep(self):
        print('私有方法')


tony = User('tony', 20, 100)

tony.say()
print(f'name is {tony.name}, age is {tony.age}, __weight为私有属性，外部不能访问')

User().say()


# 继承
'''
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>


class DerivedClassName(xxxModule.BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

# 多继承
# 若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索。
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
'''
class Student(User):

    school = None

    def __init__(self, name, age=None, weight=None, school=None):
        User.__init__(self, name, age, weight)
        self.school = school

    # 覆写父类方法
    def say(self):
        print(f'name is {self.name}, school is {self.school}')

stu = Student(name='tony', school='北大')
stu.say()

# super() 函数是用于调用父类(超类)的一个方法
super(Student, stu).say()


