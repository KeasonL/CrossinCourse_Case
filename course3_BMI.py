# 3. BMI 指数测试

weight = float(input('请输入体重（公斤）：'))
height = float(input('请输入身高（米）：'))

height_square = height ** 2
bmi = weight / height_square
min_weight = height_square * 18.5
max_weight = height_square * 24

print('您的BMI指数为： %.2f ' % bmi)
print('正常体重范围是%.2f公斤 - %.2f公斤 之间' %(min_weight, max_weight))
if bmi < 18.5:
    print('体重偏轻')
    print('建议您至少增重 %.2f 公斤' % (min_weight - weight))
elif bmi >= 24:
    print('体重偏重')
    print('建议您至少减重 %.2f 公斤' % (weight - max_weight))
else:
    print('体重正常')
