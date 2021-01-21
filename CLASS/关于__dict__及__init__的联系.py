#以下内容来自《自学是门手艺--李笑来》3.2.2类Python的实现 第265题
#编写日期:2021-1-21 13:48
class Person:
    def __init__(self, id):
        self.id = id

obama = Person(100)

obama.__dict__["age"] = 49
print(obama.age + len(obama.__dict__))
help(obama)
print(obama.__dict__)
#可以看出，这东西变成了一个字典
print(obama.__init__)
obama.__dict__["id"] = 8
print(obama.__dict__)
#可以看出，我们可以通过字典的方式从外部更新__init__的self.xxx变量
