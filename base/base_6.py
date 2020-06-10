# @File  : base_6.py
# @Author: yangbaihua
# @Date  :  2020/06/10 22:03

"""
函数
"""
def addWord(sentence):
    newString = sentence + ' please'
    return newString

def say_hello(n):
    for x in range(0,n):
        print('Hello!')

if __name__ == '__main__':
    print(addWord('Stand up'))
    say_hello(7)
