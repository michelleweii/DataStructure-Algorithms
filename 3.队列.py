# 取元素的端叫做队头，添加元素的端叫做队尾
class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        """往队列中添加一个item元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0) # 先进先出
        

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []


    def size(self):
        """返回队列的大小"""
        return len(self.__list)

# 双端队列，两端都可以进和出，相当于两个栈底部合在了一起
class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列头部添加一个item元素"""
        self.__list.insert(0,item)

    def add_rear(self, item):
        """往队列尾部添加一个item元素"""
        return self.__list.append(item)  # 先进先出

    def pop_front(self):
        """往队列头部删除一个元素"""
        return self.__list == self.__list.pop(0)

    def pop_rear(self):
        """往队列尾部删除一个元素"""
        return self.__list == self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)



if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    # 双端队列
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
