# 创建列表，列表所包含的元素可以改变
my_list = [1.0, 'Python', 3.4]
print(my_list)
# 创建元组，元组一旦创建，它所包含的元素不能修改
my_tuple = (1.2, 'Python', 3.0)
print(my_tuple)
# 如果创建的元组只有一个元素，一定要在元素的后面添加逗号
single_tuple_err = ('Python')
print(single_tuple_err)
single_tuple = ('Python', )
print(single_tuple)

# 用List()创建列表
my_list2 = list(range(2, 10))
print(my_list2)

# 用tuple()创建元组
my_tuple2 = tuple(range(1, 15))
print(my_tuple2)

# 将元组转为列表
list2 = list(my_tuple2)
print(list2)
# 将列表转为元组
tuple2 = tuple(my_list2)
print(tuple2)