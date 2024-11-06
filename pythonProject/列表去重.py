import itertools
import random
# 使用列表推导式来创建一个包含重复元素的列表
src_list = [random.randint(20,30) for i in range(15)]
print(src_list)
'''
# 用新列表搜集：只搜集不重复元素
target_list = [] # 空列表
# 遍历源列表中的每个元素
for ele in src_list:
    # 如果新列表不含当前元素，新列表添加该元素即可
    # 这样保证重复的元素第一次添加之后就添加不进去
    if ele not in target_list:
        target_list.append(ele)
'''
'''
# 将源列表传给set集合，自动去除重复元素,再回复成列表
target_list = list(set(src_list))
print(target_list)
'''
# 首先必须对列表进行排序
src_list.sort()
# 进行分组：相同的元素就分成同一组，因此不同的组当然就是不用的元素
it = itertools.groupby(src_list)
# 遍历各组，因此得到不同的元素
for k,g in it:
    print(k, list(g))
