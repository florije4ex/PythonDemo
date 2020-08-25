# @File  : 1_1_break_the_sequence_into_individual_variables.py
# @Author: yangbaihua
# @Date  :  2020/08/25 21:29

class BreakSequenceIntoIndividualVar:
    #元组
    def break_tuple_into_individual_variables(p):
        #p = (4, 5)
        x,y = p
        print("print x:",x)
        print("print y:",y)

    #列表
    def break_list_into_separate_variables():
        data = ['ACME',50,91.1,(2012,12,21)]
        name,shares,price,data = data
        print("name:",name)
        print("shares:",shares)
        print("price:",price)
        print("data:",data)

    #可迭代的，就可以执行分解操作
    #分解字符串
    def break_string_into_separate_variables():
        s = "Hello"
        a,b,c,d,e = s
        print("a=",a)
        print("b=",b)
        print("c=",c)
        print("d=",d)
        print("e=",e)

    #解压一部分，丢弃其他的值，使用任意变量名去占位，到时候丢掉这些变量就行了
    #保证选用的占位变量名在其他地方没被使用到
    def decompose_part_and_discard_others():
        data = ['ACME',50,91.1,(2012,12,21)]
        _,shares,price,_=data
        print("shares:", shares)
        print("price:", price)

if __name__ == '__main__':
    cls = BreakSequenceIntoIndividualVar()
    p = (4,5)
    cls.break_tuple_into_individual_variables(p)
    #cls.break_tuple_into_individual_variables((4,6,7)) #报错  数量不匹配
    cls.break_list_into_separate_variables()
    cls.break_string_into_separate_variables()
    cls.decompose_part_and_discard_others()


