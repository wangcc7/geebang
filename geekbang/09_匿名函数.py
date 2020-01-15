
#嵌套函数的例子
# def my_func(message):
#     print('Got a message: {}'.format(message))
#
#     # 调用函数my_func()
# my_func('Hello World')# 输出Got a message: Hello World



# def factorial(input):
#     # validation check
#     if not isinstance(input, int):  #判断一个参数的类型
#         raise Exception('input must be an integer.')   #raise 抛出异常
#     if input < 0:
#         raise Exception('input must be greater or equal to 0' )
#     ...
#
#     def inner_factorial(input):
#         if input <= 1:
#             return 1
#         return input * inner_factorial(input-1)
#     return inner_factorial(input)


#print(factorial(3))

#匿名函数的实例

#print([(lambda x: x*'*')(x) for x in range(10)])
# 输出

#输出的实例

# from tkinter import Button, mainloop
# # button = Button(
# #     text='This is a button',
# #     command=lambda: print('being pressed')) # 点击时调用lambda函数
# # button.pack()
# # mainloop()


d = {'mike': 10, 'lucy': 2, 'ben': 30}
print(d.items())
sorted(d.items(), key=lambda x: x[1], reverse=True)

#lamdba 数据清洗的样例
# data["工作日"] = data["日期"].map(lambda x: x.weekday())
# data["工作日"] = data["工作日"].map(lambda x: 1 if x<5 else 0)