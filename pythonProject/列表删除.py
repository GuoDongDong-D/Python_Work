my_list = ['python', "C++", 'java', 'js', "Qt"]
del my_list[2]
print(my_list)

my_list.extend(range(20, 26))
print(my_list)

del my_list[5:7]
print(my_list)

del my_list[2:7:2]
print(my_list)
