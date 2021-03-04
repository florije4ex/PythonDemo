# @File    : list_de_duplication
# @Description:列表去重
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2021/3/1 14:21

datalist = [6,1,2,5,2,5,2,3,6,2,9]

# 第一种，利用字典的fromkeys() 和 keys()方法
def use_dict_method(datalist):
    print(datalist) # [6, 1, 2, 5, 2, 5, 2, 3, 6, 2, 9]
    # 创建一个空字典
    d = {}
    datalist = d.fromkeys(datalist)
    print(datalist) # {1: None, 2: None, 5: None, 3: None, 6: None, 9: None}
    datalist = datalist.keys()
    print(datalist) # dict_keys([1, 2, 5, 3, 6, 9])
    datalist = list(datalist)
    print(datalist) # [1, 2, 5, 3, 6, 9]
    datalist.sort(reverse=True) # 默认升序，True 降序
    print(datalist) # [9, 6, 5, 3, 2, 1]

# 第二种方法，set集合，集合可迭代
def use_set_method(datalist):
    print(datalist) # [6, 1, 2, 5, 2, 5, 2, 3, 6, 2, 9]
    datalist_set = set(datalist)
    print(datalist_set) # {1, 2, 3, 5, 6, 9}
    datalist_list = list(datalist)
    print(datalist_list) # [6, 1, 2, 5, 2, 5, 2, 3, 6, 2, 9]

# 第三种方法，用for循环
def user_for_loop(datalist):
    print(datalist) # [6, 1, 2, 5, 2, 5, 2, 3, 6, 2, 9]
    result_datalist = []
    for i in datalist:
        if i not in result_datalist:
            result_datalist.append(i)
    print(result_datalist) # [6, 1, 2, 5, 3, 9]
    result_datalist = set(result_datalist)
    print(result_datalist) # {1, 2, 3, 5, 6, 9}

if __name__ == '__main__':
    # use_dict_method(datalist)
    use_set_method(datalist)
    # user_for_loop(datalist)