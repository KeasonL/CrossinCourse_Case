# 6. 生成优惠券号码

import random
import string

for i in range(0, 200):
    # 使用默认的52个字符列表（26个字母，大小写）并转换成list
    a = list(string.ascii_letters)
    # 使用shuffle函数把list乱序
    random.shuffle(a)
    # 取乱序后的list的前8个字符连接成字符串，打印到屏幕
    print(''.join(a[:8]))