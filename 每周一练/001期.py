
#文件编写目的:系统通知中的第001期每周一练。活动日期：北京时间 2021-01-19 12:00 至 01-26 12:00
#题目：
#请实现:获取指定路径的所有文件列表，识别出有哪些文件类型，不同类型的文件分别有多少个？
#如果在 xue.cn 上直接运行，指定路径为 todo_dir = './the-craft-of-selfteaching'
#掌握 linux 或 mac 或 windows 操作系统文件路径表示方法的区别

#掌握 os.walk() 获取指定路径的所有文件列表

#掌握 str.split() 或 os.path.splitext() 识别文件类型

#掌握 str.endswith() 判断文件类型

#掌握构造字典来存储和更新类型及其数量

#训练“获取新知时，不懂就搜索”的自学习惯

#训练“积累实战经验时，反复练习直至掌握”的自学习惯

#注意使用三个'号的地方可能下次运行时需要删除后再添加才能正常运行，原因是空格制表符的问题。
#以下为程序正文。

import os
def filesearch(path):
  '''
  编写日期:2021-1-19 22:57
  函数功能：用于查询path路径下存在.py .js .txt文件的个数
  参数:path--路径名
  '''
  filetype=('.py','.js','.txt')
  py_File_count=0
  js_File_count=0
  txt_File_count=0
  for roots,dirnames,filenames in os.walk(path):
    for filename in filenames:
      if filename.endswith(filetype[0]):
        py_File_count=py_File_count+1
        print(roots+"\\"+filename)
      elif filename.endswith(filetype[1]):
        js_File_count=js_File_count+1
        print(roots+"\\"+filename)
      elif filename.endswith(filetype[2]):
        txt_File_count=txt_File_count+1
        print(roots+"\\"+filename)
  return (py_File_count,js_File_count,txt_File_count)


def filesearchAll(pathDir):
  '''
  编写日期:2021-1-19 22:57
  函数功能：用于查询path路径下所有的文件
  参数:path--路径名
  '''
    for roots,dirnames,filenames in os.walk(pathDir):
      for filename in filenames:
        print(roots+'\\'+filename)
        
todo_dir = './the-craft-of-selfteaching'
File_Count=filesearch(todo_dir)
print('.py文件个数为:',File_Count[0])
print('.js文件个数为:',File_Count[1])
print('.txt文件个数为:',File_Count[2])
print(' ')
print('以下为该路径下的全部文件:')
filesearchAll(todo_dir)
