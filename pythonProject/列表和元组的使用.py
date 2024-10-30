'''序列得访问方式：
    1、正向访问
    2、反向访问
'''

my_tuple = tuple(range(3, 10))
print(my_tuple)
# len()访问元组的长度
print(len(my_tuple))
print(my_tuple[1])  # 访问第二个元素
print(my_tuple[-2])  # 访问倒数第三个元素

my_list = ["C语言", "C++", "Java", "Python", "C#", "GO", 6.0]
print(my_list[1])
print(my_list[0:5:1])
'''列表只能和列表相加，元组只能和元组相加'''
list1 = [20, 'Python']
list2 = list(range(1, 8))
print(list1 + list2)

tuple1 = ("Python", 2.8, 3.0)
tuple2 = tuple(range(5, 9))
print(tuple1 + tuple2)
'''列表乘法'''
# 序列只能与整数相乘，就是把元素重复N次
list1 = ['python', 29, -2]
print(list1*3)
