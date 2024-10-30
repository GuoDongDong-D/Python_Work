# Python会将多个值封装为元组，然后将元组幅值给变量
my_data = 23, 34, 454, 656, 77, 23.9, "df"
print(type(my_data))
print(my_data)
'''Python自动解包'''
#   自动解包，序列中的四个值自动赋值给四个变量a b c d
my_list = [20, 'pyhon', 3.3, False]
a, b, c, d = my_list
print(a, b, c, d)

#   所有序列（甚至包括range）都能自动解包
e, f, g = range(20, 23)
print(e, f, g)