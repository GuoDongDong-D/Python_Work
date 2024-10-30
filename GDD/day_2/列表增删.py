import math
# 在列表末尾添加元素
motorcycles=['holes', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('hhhhh')
print(motorcycles)
# append()动态创建列表
# 在列表中插入元素
motorcycles.insert(0, 'Hello')
print(motorcycles)

# 在列表中删除元素
del motorcycles[3] # 永久性删除
print(motorcycles)
# 删除最后一个元素使用pop函数
motorcycles.pop()
print(motorcycles)
# 删除指定索引元素
motorcycles.pop(0)
print(motorcycles)
# 根据值删除元素，使用remove()方法
motorcycles.remove("hhhhh")
print(motorcycles)
