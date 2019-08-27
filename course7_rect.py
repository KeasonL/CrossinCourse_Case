# 7 打印图案

def rect(a=5, b=5, c='*'):
    for i in range(a):
        print(c * b)

rect()
rect(4, 3)
rect(2, 6, '!')
