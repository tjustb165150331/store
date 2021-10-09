import random
import time
jb = 5000
hh = 0
randint = random.randint(1, 60)
while True:
    if jb >0:
        num = input("请输入一个数字")
        if num.isdigit():
            num = int(num)
            if num == randint:
                print("正确，荣获金币3000个")
                jb = jb + 3000
                hh = hh + 1
            elif num > randint:
                print("猜大了")
                jb = jb - 500
                hh = hh + 1
                print("剩余金币为：", jb)
            elif num < randint:
                print("猜小了")
                jb = jb -500
                hh = hh + 1
                print("剩余金币为：", jb)
        else:
            print("别乱输入其他的")
    else:
        print("金币输光了，游戏结束")
    if hh%3==0:
        time.sleep(5)
    if hh == 15:
        print("猜错了15次，游戏锁定")
        while True:
            pass








