# 数据结构要形成一个整体是面向对象的概念

# 节点实现
"""
c中*代表地址，python中没有特殊的变量代表地址。so...
python中交换两个变量（只有python中是这样的）。
a = 10
b = 20
a,b = b,a # 最终改变的是a,b的指向，ab仅仅是名字。在python中一切皆对象。
"""
class Node(object):
    """节点"""
    # 构造函数
    def __init__(self,elem):
        self.elem = elem
        self.next =  None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        # 对外来说，不需要知道头结点这个属性，
        # 内部使用，不暴露所以要私有化
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head==None

    def length(self):
        """遍历整个链表"""
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 1
        while cur!=None:
            count+=1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            # if: cur.next!=None,会丢掉最后一个元素。
            print(cur.elem)
            cur = cur.next

    def add(self,item):
        """链表头部添加元素"""
        

    def append(self,item):
        """链表尾部添加元素"""

    def insert(self,pos,item):
        """指定位置添加元素"""

    def remove(self,item):
        """删除节点"""

    def search(self,item):
        """查找节点"""


