# import 4-1.单链表
# 这样，以下的4个方法都可以直接继承——代码复用
class Node(object):
    """节点"""
    def __init__(self,item):
        self.elem = item
        self.prev = None
        self.next = None

class DoubleLinkList(object):
    """双向链表"""
    def __init__(self, node=None):
        # 对外来说，不需要知道头结点这个属性，
        # 内部使用，不暴露所以要私有化
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

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

# 添加，删除是新的
    def add(self, item):
        """链表头部添加元素, 头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:  # 默认为头插
            self.add(item)
        elif pos > (self.length() - 1):  # 默认为尾插
            self.append(item)
        else:
            # pre = self.__head
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur=cur.next
                # pre = pre.next
            # 当循环退出后，pre指向pos的位置
            node = Node(item)
            # node.next = pre.next
            # pre.next = node
            # 1.
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            """
            # 2.
            node.next=cur
            node.prev=cur.prev
            cur.prev=node
            cur.prev.next=node
            """

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        # pre = Node
        while cur != Node:
            if cur.elem == item:
                # 先判断此节点是否是头结点
                # 头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next: # 如果只有一个节点，且删除它
                        cur.next.prev = None
                else:
                    # pre.next = cur.next
                    cur.prev.next = cur.next
                    if cur.next: # 如果不是最后一个节点
                        # 因为最后一个节点的next已经是none了。
                        cur.next.prev = cur.prev
                break
            else:
                # pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点"""
        cur = self.__head
        while cur != Node:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.add(8)  # 8 1 2 3 4 5
    dll.insert(-1, 9)  # 9 8 1 2 3 4 5
    dll.travel()
    dll.insert(2, 100)  # 9 8 100 1 2 3 4 5
    dll.travel()
    dll.insert(10, 200)  # 9 8 100 1 2 3 4 5 200
    dll.travel()
    dll.remove(100)  # 9 8 1 2 3 4 5 200
    dll.travel()
    dll.remove(200)  # 9 8 1 2 3 4 5
    dll.travel()
    dll.remove(9)  # 8 1 2 3 4 5

    dll.travel()
