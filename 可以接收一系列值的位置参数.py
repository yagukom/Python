#2021-1-7
#以下联系来自《自学是门手艺--李笑来》2.4.2关于参数（下）的编程题116
#题目：使用可以接收一系列值的位置参数编写代码，使得代码的输出结果为： Hello，mike! Hello，john! Hello，zeo!


def Say_Hello(*names):
  for name in names:
  	print("Hello,",name)

def Say_Hi(*names):#当不使用类似于Say_Hello(*names)中的for循环遍历时，会输出一个元组
  print("Hi,",names)
  
Names0=["mike","john","zeo"]#列表List使用[]来定义
Names1=("ahra","dina","terisa")#元组Tuple使用()来定义

#List 是可变有序容器，Tuple 是不可变有序容器。
#初学者总是很好奇 List 和 Tuple 的区别。首先是使用场景，在将来需要更改的时候，创建 List ；
#在将来不需要更改的时候，创建 Tuple。其次，从计算机的角度来看，Tuple 相对于 List 占用更小的内存。
#以上注解选自《自学是门手艺--李笑来》1.5.6数据容器--元组
Say_Hello(*Names0)
Say_Hi(*Names0)
print('\n')
Say_Hello(*Names1)
Say_Hi(*Names1)
