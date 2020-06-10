# @File  : base_4.py
# @Author: yangbaihua
# @Date  :  2020/06/10 21:35
"""
字符串
"""
if __name__ == '__main__':
    #字符串
    bookName = "My Python World"
    print(bookName)
    #字符串的方法
    print(len(bookName))
    #方括号，从0开始
    print(bookName[0])
    #超过字符串长度
    #print(bookName[33])
    #截取字符串
    print(bookName[:9])
    print(bookName[10:])
    #+连接字符串
    print("Welcom to "+bookName)