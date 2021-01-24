import re
with open(r'hanhan.txt.txt','r') as f:#如果在Windows下使用绝对路径的话，注意这里需要使用转义符r
    str = f.read()
pttn = r'beg[iau]ns?'
print(re.findall(pttn, str))
