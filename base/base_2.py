# @File  : base_2.py
# @Author: yangbaihua
# @Date  :  2020/05/23 10:21

print("布尔值")
print(True)
print(False)
print(1<2)
print(2<1)

print(True and True)
print(True and False)
print(not True)

print(True or False)
print(not False)

print(3>5 or 3<4)
print(3>5 and 3<4)

print("请输入年龄：")
age = input()
if int(age)>=18:
    print("你输入是：adult")
else:
    print("你输入是：teenager")
