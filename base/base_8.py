# @File    : base_8
# @Author  : yangbaihua
# @Time    : 2020/6/11 9:58

import random

def WhileDemo():
    count = 1
    randomNumber1 = 0
    randomNumber2 = 0
    #两个骰子不等于6会一直循环
    while not (randomNumber1 == 6 and randomNumber2 == 6):
        randomNumber1 = random.randint(1,6)
        randomNumber2 = random.randint(1,6)

        total = randomNumber1 + randomNumber2
        print("第",count,"次打印两个骰子的和为：",total)
        #首先判断两个数是否相等的
        if randomNumber1 == randomNumber2:
            print("第",count,"次Double")
            break
        else:
            #如果不相等，在判断两个数之和的大小
            if total > 8:
                print("第",count,"次Big")
            elif total > 4:
                print("第",count,"次Not Bad")
            else:
                print("第",count,"次Small")
        count+=1
if __name__ == '__main__':
    WhileDemo()