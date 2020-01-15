# -*- coding: utf-8 -*-
# by wangcc
# mail:wangcc_sd@163.com


class Document():
    def __init__(self, title, author, context):
        print('-------init function called-------')
        self.title = title
        self.author = author
        self.__context = context # __开头的属性是私有属性

    def get_context_length(self):
        print(self.title)
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

#print(harry_potter_book.title)
#print(harry_potter_book.author)
#print(harry_potter_book.get_context_length())
#
# harry_potter_book.intercept_context(10)
#
# print(harry_potter_book.get_context_length())
#
# print(harry_potter_book.__context)

########  继承
#实体类
class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)

#文档
class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self,"document")
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)

#电影
class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_movie.object_type)

harry_potter_book.print_title()
harry_potter_movie.print_title()
print("*" * 20)
print(harry_potter_book.get_context_length())
print(harry_potter_movie.get_context_length())

########## 输出 ##########
'''
类： 一群有着相同属性和函数(方法)的对象(实例)的集合，也可以具象化的理解为是一群有着相似特征的事物的集合；用class来声明。
抽象类：是一种特殊的类，只能作为父类存在，一旦对象化（或叫实例化）就会报错；一般使用class Classname(metaclass=ABCMeta)来声明。
类的继承：子类继承父类，子类可以使用父类的属性和函数，同时子类可以有自己独特的属性和函数；子类在生成对象的时候（实例化时），是不会自动调用父类的构造函数的，必须在子类的构造函数中显示的调用父类的构造函数；继承的优势是减少重复代码，降低系统熵值（即复杂度）。

属性：用"self.属性名"来表示，通过构造函数传入；表示对象(实例)的某个静态特征。
私有属性：以__开头的属性，举例：self.__属性名，只能在类内部调用，类外部无法访问。
公有属性：和函数并列声明的属性，可以理解为常量，一般用全大写表示；在类中通过"self.常量名"来调用，在类外使用"对象名.常量名"或者"类名.常量名"来调用。

函数：表示对象(实例)的某个动态能力。
构造函数：用def __init__（self, args...）声明，第一个参数self代表当前对象的引用，其他参数是在对象化时需要传入的属性值；构造函数在一个对象生成时(即实例化时)会被自动调用。
成员函数：是正常的类的函数，第一个参数必须是self；可通过此函数来实现查询或修改类的属性等功能。
静态函数：静态函数和类没有什么关联，第一个参数也没有什么特殊性；一般用来做一些简单独立的任务，既方便测试也能优化代码结构；一般使用装饰器@staticmethod来声明。
类函数：类函数的第一个参数一般为cls，表示必须传一个类进来；最常用的功能是实现不同的init构造函数；需要装饰器@classmethod来声明。
抽象函数：一般定义在抽象类中，主要目的是要求子类必须重载该函数才能正常使用；使用装饰器@abstractmethod来声明。
函数重载：父类的某函数通过raise Exception的方式要求子类必须重写该函数来覆盖父类原有函数。
对象：类对象化(实例化)后的某一个具体事物。
'''