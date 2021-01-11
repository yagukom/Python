#2021-1-11 9:22
#题目来自《自学是门手艺--李笑来》2.4.4递归函数 编程题1165
#递归函数实现反向打印字符
#昨天晚上写的是用for循环实现反向打印字符.py
def StringReverseCoreFunc(string,StringIndex,ResultString):#2字符串反向打印的核心递归函数
  """
  2021-1-11 11:26
  用于字符串反向打印的递归函数。
  参数1:为用户最初从input()输入的字符串。
  参数2:为参数1字符串的下标。
  参数3:为每次该递归函数处理后的列表型的字符串结果。
  """
  if StringIndex==0:
    #result.append(string[length])此行多余，因为会重复输出最后一个字符
    print("List形式的结果:",ResultString)
    RealResultString=''.join(ResultString)
    print("String形式的结果",RealResultString)
  else:
    ResultString.append(string[StringIndex-1])
    StringIndex=StringIndex-1 #递归函数的参数里肯定有一个参数是拿来计数的
    print("执行的字符串下标值：",StringIndex)
    StringReverseCoreFunc(string,StringIndex,ResultString)
  
def StringReverse(string):#1字符串反向打印的入口函数
    MirrorString=[]
    length=len(string)
    StringReverseCoreFunc(string,length,MirrorString)#2进入核心递归函数
  
InputString=input("请输入：")
StringReverse(InputString)#0
help(StringReverseCoreFunc)#这一行和下一行是为了显示Docstring的内容的。
print(StringReverseCoreFunc.__doc__)#这部分的内容来自于《自学是门手艺李笑来》2.4.5函数的文档。
