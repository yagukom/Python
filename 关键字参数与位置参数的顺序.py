#2021-1-7 15:51
#请修改以下代码中的错误：

#def make_sentence(name="Ann",age,sex="boy"):
#    print(f"{name} is {age} years old and is a {sex}.")

#make_sentence("Kate","8","girl")
#make_sentence(name="Mike","9","boy")
#make_sentence(age="8",name="Jiaming",sex="boy")

#请特别留意关键字参数与位置参数的特性。完成这道习题时遇到困难，可反复重读《1.5.4 函数》这一节内容。

def make_sentence(age,name="Ann",sex="boy"):
    print(f"{name} is {age} years old and is a {sex}.")

make_sentence("Kate","8","girl")
make_sentence("9",name="Mike",sex="boy")
make_sentence(age="8",name="Jiaming",sex="boy")
