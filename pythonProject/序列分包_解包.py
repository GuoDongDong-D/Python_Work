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
# 如果你只解包中的某几个值，剩下的值可用带*的变量（列表）来接收
first, *rest, last = my_list
print(first)
print(rest)
print(last)

# 如果你只解包中的某几个值，剩下的值可用带*的变量（列表）来接收
first, second, *rest = my_list
print(first)
print(second)
print(rest)

# 字符串本身也是序列，也支持解包
a, b, *c ="fasjiefa"
print(a)
print(b)
print(c)
# 多变量同事赋值
a, b, c = "sf", 30, list(range(1, 4))
print(a)
print(b)
print(c)
