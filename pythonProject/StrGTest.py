s = "fjkjkl.gos"
# 根据下标访问
print(s[5])
# 指定开始、结束
print(s[2:4])
# 指定开始、结束、间隔（步长）
print(s[1:8:2])

# in运算符判断是否包含某个字符串
print("gos" in s)
print("goj" in s)
# len()获取字符串长度
print(len(s))
# min()获取字符串中最小字符
print(min(s))
# max()获取字符串中最大字符
print(max(s))
# 字符串方法
print(s.upper())
print(s.lower())
print(s.title())
# dir()查看类或模块的所有方法
print(dir(str))
print(s.islower())
print("skdkfF".islower())

s = " sfsfeg "
# 删除两边的空白
print(s.strip())
# 删除左边的空白
print(s.lstrip())
# 删除右边的空白
print(s.rstrip())

# 复杂的数学运算可以使用math模块
import  math
print(math.sin(3.14/4))
