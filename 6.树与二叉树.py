# 广度优先遍历==用队列实现
class Node(object):
    # 树节点是对链表的扩充
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        # 最后去添加，不考虑头插还是尾插
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                # 左节点为空，新加入的节点放到这个位置上
                cur_node.lchild=node
                return
            else:
                # 不是空的话，左节点入队
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        # 广度（层次）遍历
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 深度遍历————（前序，中序，后序）
    def preorder(self,node):
        if node is None:
            return
        print(node.elem,end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    # 中序+前or后任意一个，就可以判断出一个树
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem,end=" ")
        self.inorder(node.rchild)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")



if __name__ == '__main__':
    tree=Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print("")
    tree.inorder(tree.root)
    print("")
    tree.postorder(tree.root)