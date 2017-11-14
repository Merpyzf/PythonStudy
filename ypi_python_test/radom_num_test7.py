import random
import sys

sys.path.append()


time = 4
min_num = 0
max_num = 20
guess = -1

secret = random(min_num, max_num)

print "----------猜数字游戏----------"

while guess != secret and time >= 1:
    guess = input("数字区间" + min_num + '-' + max_num + ',请输入你猜的数字')
    print '你输入的数字是: ' + guess
    if guess == secret:
        break
    else:
        if guess < secret:
            min_num = guess
        else:
            max_num = guess

time = time - 1
