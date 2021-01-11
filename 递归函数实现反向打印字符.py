#2021-1-11 9:22
#题目来自《自学是门手艺--李笑来》2.4.4递归函数 编程题1165
#递归函数实现反向打印字符
#昨天晚上写的是用for循环实现反向打印字符.py
def StringReverseCoreFunc(string,length,ResultString):#2字符串反向打印的核心递归函数
  if length==0:
    #result.append(string[length])此行多余，因为会重复输出最后一个字符
    print("List形式的结果:",ResultString)
    RealResultString=''.join(ResultString)
    print("String形式的结果",RealResultString)
  else:
    ResultString.append(string[length-1])
    length=length-1 #递归函数的参数里肯定有一个参数是拿来计数的
    print("执行的字符串下标值：",length)
    StringReverseCoreFunc(string,length,ResultString)
  
def StringReverse(string):#1字符串反向打印的入口函数
    MirrorString=[]
    length=len(string)
    StringReverseCoreFunc(string,length,MirrorString)#2进入核心递归函数
  
InputString=input("请输入：")
StringReverse(InputString)#0
