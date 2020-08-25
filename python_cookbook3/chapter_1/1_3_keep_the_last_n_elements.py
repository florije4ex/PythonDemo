# @File  : 1_3_keep_the_last_n_elements.py
# @Author: yangbaihua
# @Date  :  2020/08/26 00:13
from collections import deque
#yidld使用 https://developer.ibm.com/zh/articles/os-cn-python-yield/

class KeepTheLastNElements:
    #下面的代码在多行上面做简单的文本匹配， 并返回匹配所在行的最后N行
    #往两端append数据，从两端pop数据
    #append 加入队列里
    #pop 移除队列
    def search(lines,pattern,history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line,previous_lines
            previous_lines.append(line)

if __name__ == '__main__':
    cls = KeepTheLastNElements
    with open(r'somefile.txt') as f:
        for line,prevlines in cls.search(f,'python',1):
            for pline in prevlines:
                print("!!!!",pline,end='')
            print("$$$$",line,end='')
            print('-'*20)