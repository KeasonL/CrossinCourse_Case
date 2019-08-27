# 9. 提取英文单词
import re  #载入正则表达式模块

f1 = open('from.txt')
data = f1.read()
f1.close()

result = re.findall('[A-z]+', data)
result.sort()

data = '\n'.join(result)

f2 = open('to.txt', 'w')
f2.write(data)
f2.close()
