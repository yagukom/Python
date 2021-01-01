# 这个 cell 集合运算图示需要安装 matplotlib 和 matplotlib-venn
# 在Windows下先要去Python官网下载Python安装包，然后安装时注意勾选PATH选项，不然安装完要自己手动配置PATH路径。
# 然后用WIN+R打开cmd，运行 python -m pip install matplotlib，安装matplotlib。
# 注意写代码可以使用Python官方自带的IDLE，而不要去使用VS2019，因为VS2019很多第三方库没有做适配，且python的版本号也跟不上官方Python的速度。
# 公司里下载的速度特别地慢，也不知道老板在搞些啥，天天动不动就在员工福利和人数上做减法。
# 以下为linux或mac中的操作，使用!进行下载pip包。
# 以下来自《自学是门手艺--李笑来》1.5.6数据容器 章节的内容。
# 2021-1-1 晴 祝今年有美好的一年，往物联网方向发展，顺便把N1也给考了，稍微准备一下考研的内容也行的，再也不想待在小企业里受气了，老板都是大傻逼。
# !pip install matplotlib
# !pip install matplotlib-venn
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

admins = {'Moose', 'Joker', 'Joker'}
moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

v = venn2(subsets=(admins, moderators), set_labels=('admins', 'moderators'))
v.get_label_by_id('11').set_text('\n'.join(admins & moderators))
v.get_label_by_id('10').set_text('\n'.join(admins - moderators))
v.get_label_by_id('01').set_text('\n'.join(moderators - admins))

plt.show()
