str1 = "Hello' Python"
print(str1)
str2 = 'Hello\' Python'
print(str2)

str3 = str1 + ' ' + str2
str4 = 'Hello'"Python"
print(str3)
print(str4)
str5 = str(3.5) + '元'
print(str5)
str6 = repr(3) + "米"
print(str6)
print(repr(str6))
s = input("请输入：")
print(s)
str7 = b'abc'
print(type(str7))

bStr = '我爱你'.encode()
print(bStr)
bStr2 = bytes("我爱你", "UTF-8")
print(bStr2)
print(type(bStr2))
bS = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'
print(bS.decode('UTF-8'))
print(type(bS))