my_list = ['python', "C++", 'java']
print(my_list)
# 为列表append元组,元组被当做整体
my_list.append(tuple(range(1, 11)))
print(my_list)
# extend()方法用于将序列中的元素添加进来
my_list.extend(range(20, 26))
print(my_list)

my_list.extend("fsfeef")  # 字符串也是序列
print(my_list)

my_list.insert(3, 'Qt')
print(my_list)