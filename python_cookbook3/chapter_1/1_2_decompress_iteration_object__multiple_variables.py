# @File  : 1_2_decompress_iteration_object__multiple_variables.py
# @Author: yangbaihua
# @Date  :  2020/08/25 21:57

# *号表达式
from locust.stats import avg

#扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的
class decompress_iteration_object__multiple_variables:
    # 排除掉第一个和最后一个分数
    def drop_first_last(grades):
        grades = sorted(grades)
        print("排序后", grades)
        first, *middle, last = grades
        print("去掉最大，最小", middle)
        return avg(middle)

    # *表达式用在列表后面，电话号码永远是列表（list），不管多少（包含0个）
    def phone_record(record):
        name, email, *phone_numbers = record
        return name, email, phone_numbers

    #*表达式用在列表开始
    def start_using_the_list(list):
        *trailing_qtrs,current_qtr = list
        trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)
        return trailing_avg,current_qtr,trailing_qtrs

    #可变长元组的序列
    def tag_tuple_sequence():
        records=[
            ('foo',1,2),
            ('bar','hello'),
            ('foo',3,4)
        ]
        def do_foo(x,y):
            print('foo',x,y)
        def do_bar(s):
            print('bar',s)
        for tag,*args in records:
            if tag == 'foo':
               do_foo(*args)
            if tag == 'bar':
                do_bar(*args)

    def split_string():
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        uname,*fields,homedir,sh = line.split(':')
        print('uname:',uname)
        print('fields:',fields)
        print('homedir:',homedir)
        print('sh:',sh)

    def ignore_list_elements():
        record = ('ACME',50,123.45,(12,18,2012))
        name,*_,(*_,year) = record
        print('name:',name)
        print('year:',year)

    def split_the_list_into_two_parts():
        items = [1,10,7,4,5,9]
        head,*tail = items
        print('head:',head)
        print('tail:',tail)

if __name__ == '__main__':
    cls = decompress_iteration_object__multiple_variables
    grades = [89, 50, 96, 46, 77, 83, 99, 54, 100, 85]
    print("原始数据,", grades)
    print("去掉最大，最小的平均值", cls.drop_first_last(grades))
    record = ('Dave', 'dave')
    # 号码
    record = ('Dave', 'dave@example.com', '1344444444', '0592-1234567', '10000')
    print('打印出来===name:%s,email:%s,phone:%s' % (
    cls.phone_record(record)[0], cls.phone_record(record)[1], cls.phone_record(record)[2]))

    #销售价格
    sales_record = [10,8,7,1,9,5,10,3]
    print('前七个月：',cls.start_using_the_list(sales_record)[2])
    print('前7个月销售额平均值：',cls.start_using_the_list(sales_record)[0])
    print('当月值：',cls.start_using_the_list(sales_record)[1])

    cls.tag_tuple_sequence()

    cls.split_string()

    cls.ignore_list_elements()

    cls.split_the_list_into_two_parts()