#关于hanhan.txt.txt见“正则表达式”这个目录下。
#本程序来源于《自学是门手艺--李笑来》3.2.4正则表达式 准备工作
import re
with open(r'hanhan.txt.txt','r') as f:#如果在Windows下使用绝对路径的话，注意这里需要使用转义符r
    str = f.read()
pttn = r'beg[iau]ns?'
print(re.findall(pttn, str))
