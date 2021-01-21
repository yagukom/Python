#以下内容来自《自学是门手艺--李笑来》3.2.2类Python的实现 第974题
#__变量名__这样书写后，这东西就不是私有变量了。
#编写日期：2021-1-21 14:19
class hanhan:
  __la__=8#不是私有变量
  __lb=10#私有变量
  __lc_=17#私有变量
  def __init__(self):
    self.__jibunn__='lalala'
    self.__teri='demaxiya'
    
p=hanhan()
print('p.__jibunn__值为:',p.__jibunn__)
print('p.__la__值为:',p.__la__)
#无法获取print('p._hanhan__la__值为：',p._hanhan__la__)
print('p._hanhan__lb值为:',p._hanhan__lb)
#无法获取print('p.__lb值为:',p.__lb)
print('p._hanhan__lc_值为',p._hanhan__lc_)
#无法获取print('p.__lc_值为:',p.__lc_)
