# @File  : base_5.py
# @Author: yangbaihua
# @Date  :  2020/06/10 21:47

"""
列表
"""
if __name__ == '__main__':
    numbers = [123,13,24,56,324,32]
    #列表长度
    print(len(numbers))
    #方括号
    print(numbers[0])
    #截取
    print(numbers[0:3])
    #列表中的某一项赋予新值
    #numbers[0]=3
    print(numbers)
    #使用+组合列表
    moreNumbers = [324,1000,999]
    print(numbers+moreNumbers)
    #列表的方法
    numbers.sort()#列表排序
    print(numbers)
    numbers.pop(1) #不传参数移除最后一项,，传参数移除指定位置的项
    print(numbers)
    numbers.insert(4,123123123123)#指定位置插入内容
    print(numbers)
    complexList = [123,'hello',['otherList',3,True]]#混合不同类型
    print(complexList)
    print(complexList[2][1])#指定第三项的某一项内容，操作二维数组的方式