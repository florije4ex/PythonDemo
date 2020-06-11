# @File    : base_7
# @Author  : yangbaihua
# @Time    : 2020/6/11 9:58

import random
def randomNumber():
    for x in range(1,11):
        randomNumber = random.randint(1,6)
        randomNumber2 = random.randint(1,6)
        total = randomNumber + randomNumber2
        #首先判断两个数是不是一样
        if randomNumber == randomNumber2:
            print("第",x,"次Doublue!")
        else:
            #如果不一样的话，判断两个数之和的大小
            if total > 8:
                print("第",x,"次Big")
            elif total > 4 and total <=8:
                print("第",x,"次Not bad")
            else:
                print("第",x,"次Small")
        print("第",x,"次打印两次的值：",total)

if __name__ == '__main__':
    randomNumber()