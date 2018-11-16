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
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node = None):
        # 对外来说，不需要知道头结点这个属性，
        # 内部使用，不暴露所以要私有化
        self.__head = node
        if node:
            # 如果链表不为空
            node.next=node

    def is_empty(self):
        """链表是否为空"""
        return self.__head==None

    def length(self):
        """遍历整个链表"""
        # cur游标，用来移动遍历节点
        if self.is_empty(): # 空链表
            return 0
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head: # 只有一个节点也满足
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            # if: cur.next!=None,会丢掉最后一个元素。
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点的元素未打印
        print(cur.elem)

    def add(self,item):
        """链表头部添加元素, 头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self.__head
            self.__head=node
            # cur.next = node
            cur.next = self.__head


    def append(self,item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next=node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            # or
            # node.next = cur.next
            # cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos<=0: #默认为头插
            self.add(item)
        elif pos>(self.length()-1): # 默认为尾插
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count<(pos-1):
                count+=1
                pre=pre.next
            # 当循环退出后，pre指向pos-1的位置
            node=Node(item)
            node.next=pre.next
            pre.next=node

    def remove(self,item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = Node
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此节点是否是头结点
                # 删除头节点，需要更改尾节点的next域
                if cur == self.__head:
                    # 头结点
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear=rear.next
                    # rear指向尾节点
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间位置
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = Node
            pre.next = cur.next

    def search(self,item):
        """查找节点"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head: # 会丢掉最后一个元素
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False



if __name__=="__main__":
    ll= SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.add(8) # 8 1 2 3 4 5
    ll.travel()
    ll.insert(-1,9) # 9 8 1 2 3 4 5
    ll.travel()
    ll.insert(2,100) # 9 8 100 1 2 3 4 5
    ll.travel()
    ll.insert(10,200) # 9 8 100 1 2 3 4 5 200
    ll.travel()
    ll.remove(100) # 9 8 1 2 3 4 5 200
    ll.travel()
    ll.remove(200) # 9 8 1 2 3 4 5
    ll.travel()
    ll.remove(9) # 8 1 2 3 4 5

    ll.travel()


