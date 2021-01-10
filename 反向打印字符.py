#2021-1-10 22:21
#原本是作为《自学是门手艺》的2.4.4递归这章节里的第1165题的“使用递归函数实现反向字符打印”的操作的
#但是太晚了就先拿for循环凑活一下，明天继续。

def StringReverse(string):
    ReversedStrList=[]
    print('length of InputString',len(string))
    for i in range(0,len(string)):
        ReversedStrList.append(string[len(string)-1-i])
    print("转换后的列表为:",ReversedStrList)
    print(type(ReversedStrList))
    ReversedStr=''.join(ReversedStrList)
    print("最终输出为:",ReversedStr)
    print(type(ReversedStr))
    
InputString=input("请输入:")
StringReverse(InputString)
