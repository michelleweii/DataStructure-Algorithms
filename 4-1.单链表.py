# 数据结构要形成一个整体是面向对象的概念

# 节点实现
class Node(object):
    """节点"""
    # 构造函数
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        # 对外来说，不需要知道头结点这个属性，
        # 内部使用，不暴露所以要私有化
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head==None

    def length(self):
        """遍历整个链表"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            # if: cur.next!=None,会丢掉最后一个元素。
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self,item):
        """链表头部添加元素, 头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表
            self.__head = node
        else:
            # 如果不是空链表
            cur = self.__head
            while cur.next != None:
                # cur一直指到末尾
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0: # 默认为头插
            self.add(item)
        elif pos>(self.length()-1): # 默认为尾插
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count<(pos-1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        # pre指向cur前面的位置
        pre = Node
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头结点
                # 头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点"""
        cur = self.__head
        while cur != Node:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



if __name__=="__main__":
    ll = SingleLinkList()
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
    ll.insert(-1,9) # 9 8 1 2 3 4 5
    ll.travel()
    ll.insert(2,100) # 9 8 100 1 2 3 4 5
    ll.travel()
    ll.insert(10,9) # 9 8 100 1 2 3 4 5 200
    ll.travel()  # 9 8 100 1 2 3 4 5 9
    ll.remove(9) # 8 100 1 2 3 4 5 9 这个remove不能删除最后一位数字
    ll.travel()
    # ll.remove(200) # 9 8 1 2 3 4 5
    # ll.travel()
    # ll.remove(9) # 8 1 2 3 4 5

    ll.travel()


