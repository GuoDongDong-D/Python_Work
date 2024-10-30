# sort()方法对列表进行永久性排序
car = ['bmw', 'audi', 'toyol', 'subar']
print(car)
car.sort()
print(car)

# 使用shorted()函数对列表进行临时性排序
car = ['bmw', 'audi', 'toyol', 'subar']
print("Here is the original list:")
print(car)
print("\nHere is the sorted list:")
print(sorted(car))
print("\nHere is the original list again:")
print(car)
# 倒着打印对象,使用reverse()方法
car.reverse()
print(car)
# 确定列表的长度len()函数
print("car list len is:")
print(len(car))