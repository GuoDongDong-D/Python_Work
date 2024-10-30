my_list = ['python', "C++", 'java', 'js', "Qt"]
my_list[-2] = 'C#' # 对单个元素赋值
print(my_list)
# 被替换部分只用两个元素，替换四个元素，实际是增加了元素
my_list[2:4] = ['lua', 'go', 'learing', 'php']
print(my_list)
# 被替换部分只用三元素，替换1个元素，实际是删除了元素
my_list[2:5] = ['object-c']
print(my_list)
# 当列表中一段幅值时，程序会自动把字符串当成列表处理
my_list[1:3] = 'fdjjkd'
print(my_list)
print(dir(list)) 