# 5 猜数字
import random

welcomestr = '''
###欢迎来到猜数字游戏###
两种游戏模式：
1、循环模式：多次游戏，统计猜中的次数
2、挑战模式：每轮可以猜8次，如果连续3轮8次内猜中，挑战升级

输入E结束游戏
'''

def guess_num1():
    print('1、循环模式：多次游戏，统计猜中的次数')
    list_c = []
    playing1 = True
    while playing1:
        secret = random.randint(0, 100)
        c = 0
        min_s = 0
        max_s = 100
        guessing = True
        while guessing:
            guess = (input('##请输入介于%d - %d之间的数字\n##放弃请按X—>' %(min_s, max_s)))
            c += 1
            try:
                if guess == 'x' or guess == 'X':
                    break
                elif int(guess) == secret:
                    list_c.append(c)
                    print('Bingo!猜了%d次，终于猜中了！' % c)
                    break
                elif int(guess) > secret:
                    print('猜的数太大了!')
                    max_s = int(guess)
                elif int(guess) < secret:
                    print('猜的数太小了!')
                    min_s = int(guess)
            except:
                print('请输入介于%d - %d之间的数字,浪费了1次机会' %(min_s, max_s))
        total_c = 0
        for cc in list_c:
            total_c += cc
        try:
            average_c = total_c / len(list_c)
            print('共猜了%d轮，平均需要%.2f次猜中！' %(len(list_c), average_c))
        except:
            print('共猜了%d轮' %len(list_c))
        ask = input('是否继续？任意键继续，N返回')
        if ask == 'n' or ask == 'N':
            playing1 = False



def guess_num2():
    print('2、挑战模式：每轮可以猜8次，如果连续3轮8次内猜中，挑战升级')
    n = 8
    row = 0 # win in row
    playing2 = True
    while playing2:
        secret = random.randint(0, 100)
        print(secret)
        min_s = 0
        max_s = 100
        if row < 3:
            x = 0
        elif row >= 3:
            x = row - 2
        for t in range(n-x):
            print('还剩%d次机会' %(n-x-t))
            guess = (input('##请输入介于%d - %d之间的数字\n##放弃请按X—>' %(min_s, max_s)))
            try:
                if guess == 'x' or guess == 'X':
                    break
                elif int(guess) == secret:
                    print('Bingo!猜了%d次，终于猜中了！' % (t+1))
                    row += 1
                    print('连续猜对第%d次' % row)
                    break
                elif int(guess) > secret:
                    print('猜的数太大了!')
                    max_s = int(guess)
                elif int(guess) < secret:
                    print('猜的数太小了!')
                    min_s = int(guess)
            except:
                print('请输入介于%d - %d之间的数字,浪费了1次机会' %(min_s, max_s))
            if t == (n-x-1):
                print('机会用尽了')
                row = 0
        if row == 10:
            print('通关了！AMAZING！！！')
        ask = input('是否继续？任意键继续，N返回')
        if ask == 'n' or ask == 'N':
            playing2 = False
    



print(welcomestr)
playing = True
while playing:
    mode = input('请选择游戏模式，输入1 或 2。退出输入E')
    if mode == 'E' or mode =='e':
        break
    elif mode == '1':
        # print('mode 1')
        guess_num1()
    elif mode == '2':
        # print('mode 2')
        guess_num2()
    else:
        print('输入无效')


print('你已输入E，游戏结束')
