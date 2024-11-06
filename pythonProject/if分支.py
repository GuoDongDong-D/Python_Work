nage = int(input("请输入一个整数："))
# 不要忘记冒号，冒号代表条件结束、执行体的开始
if nage % 2 == 0:
    print(nage)
s = 'Hello world!'
if s:
    print(s)
# 所有代表空的值，如0、''、 []、 ()、 {}、 None都会被当成False处理

score = int(input("请输入您的成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print('中等')
elif score >= 60:
    print("及格")
else:
    print('不及格')