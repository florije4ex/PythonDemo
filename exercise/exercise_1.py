# @File  : exercise_1.py
# @Author: yangbaihua
# @Date  :  2020/06/10 22:12
"""
猜词游戏
"""
import random
#创建词库
words = ['chicken','dog','cat','mouse','frog','rabbit']
guessTimes = 14
def pickWord():
    return random.choice(words)

def play():
    word = pickWord()
    while True:
        guess = getGuess(word)
        if processGuess(guess, word):
            print('You win!')
        if guessTimes == 0:
            print('Game over!')
            print('The word was: ' + word)
            break

def getGuess(word):
    printWordWithBlanks(word)
    print('Guess Times Remaining：' + str(guessTimes))
    guess = input(' Guess a latter?/n')
    return guess

def printWordWithBlanks(word):
    print('not done yet')

def processGuess(guess,word):
    global guessTimes
    guessTimes = guessTimes - 1
    return False

if __name__ == '__main__':
    play()