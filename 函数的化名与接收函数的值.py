#2021-1-7 16:56
#内容来自《自学是门手艺--李笑来》2.4.3化名与匿名 习题117

def is_f():
    return 'value'
name_1 = is_f
name_2 = is_f()
print(name_1 == name_2)
print(name_1() is name_2)

#结果为：
# False
# True
