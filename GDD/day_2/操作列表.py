# 遍历整个列表
magicians = ['alice', "david", 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see you next trick, " + magician.title() + "\n")
print('Thank you, everyone. That was a great magic show!')
# 创建数值列表使用函数range()
for value in range(1, 8):
    print(value)
# 使用range()创建数字列表
numbers = list(range(5, 9))
print(numbers)
event_numbers = list(range(11, 20, 2))
print(event_numbers)
# 将10个整数的平方加入到一个列表中
squars = []
for value in range(1, 11):
    squar = value ** 2
    squars.append(squar)
print(squars)
# 对数字列表执行简单的统计计算
# 1、列表解析
squares = [value**2 for value in range(5, 11)]
print(squares)
# 切片
plays = ['charls', 'martins', 'michal', 'florence', 'ceill']
print(plays[0:3])
print(plays[2:5])
# 如果不指定第一个索引，Python将自动从列表头开始
print(plays[:4])
# 如果不指定第二个索引，Python将终止与列表末尾
print(plays[2:])
# 遍历切片
print("Here are the first three players on my team:")
for player in plays[:3]:
    print(player.title())
# 元组
my_tuple = tuple(range(1, 5))
print(my_tuple)
# len()函数可以访问列表的长度
print(len(my_tuple))
print(my_tuple[1:3])
print(my_tuple[2])
my_list = ['python', 'java', 'C++', 'C#']
print(my_list)
print(my_list[2])
print(my_list[-2])