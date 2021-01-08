#2021-1-8 14:52
#以下来自https://www.runoob.com/python/att-list-sort.html
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)#即比较的是第二个元素。
# 输出类别
print('排序列表：', random)



#以下来自以下内容来自《自学是门手艺--李笑来》2.4.3化名与匿名：（应该称为函数名的化名与匿名才对）
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
#因为是以pairs中的一个个(...,...)进行传输的，故这里比较的其实是(...,...)中的第二个内容，即'one','two'这些字符串
#可以通过阅读上方2~13行的内容进行完全的理解。
pairs
