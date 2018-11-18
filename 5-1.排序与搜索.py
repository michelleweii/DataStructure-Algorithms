# 冒泡排序
# 外层循环控制走多少次
# 内层循环控制从头走到尾
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        # j是[0,1,2,3,...,n-2]
        count = 0
        for i in range(0,n-1-j):
            # 班长从头走到尾
            if alist[i]>alist[i+1]: # 升序
                alist[i],alist[i+1]=alist[i+1],alist[i]
        if 0==count: # 如果没有进行交换（代码优化），变成O(n)--内层循环走一遍
            return

# i: 0~n-2  range(0,n-1)  j=0
# i: 0~n-3  range(0,n-1-1) j=1
# i: 0~n-4  range(0,n-1-2) j=2
# j=n i range(0,n-1-j)

# # 冒泡方法二：
# for j in range(len(alist)-1,0,-1):
#     # j是[n-1,n-2,n-3,n-4,...]
#     for i in range(j):



# 选择排序———认为数组有两部分，前一部分是有序的，后一部分是无序的（操作后半部分）
# 遍历一遍，找到最小值，和无序部分的第一个值交换，然后将这个值加入有序部分
def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1): # j:0~n-2，先看内层循环
        min_index = j
        for i in range(j+1, n):
            if alist[min_index]>alist[i]:
                min_index=i
        # 找到最小值的下标之后，进行交换
        alist[j],alist[min_index]=alist[min_index],alist[j]

# 插入算法———拿无序序列的第一个元素，和前面有序序列进行比较。（操作前半部分）
def insert_sort(alist):
    """插入排血"""
    n=len(alist)
    for j in range(1,n):
        # i=[1,2,3, ... ,n-1]
        # i 代表内层循环起始值
        i=j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中。
        while i>0:
            # i=j j-1 j-2 ... 1
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            else: # 优化 O(n)
                break

# 希尔排序__插入算法的改进版本gap=1时
def shell_sort(alist):
    n = len(alist)
    gap = n // 2 # 起始从gap开始的
    # 4，2，1 或者9，6，1，如何达到最优？ 数学知识，不做研究
    # gap 变化到0之前，插入算法的执行次数
    while gap >= 1:
        # 希尔与普通的插入算法的区别就是gap步长
        for j in range(gap,n):
            # 所有子序列的所有元素
            i = j
            while i > 0:
                # 内循环执行的是：插入算法的比较和交换
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2





# 快速排序
def quick_sort(alist):
    """快速排序"""
    mid_value = alist[0]
    n=len(alist)
    low=0
    high=n-1
    while low<high:
        if alist[high]>mid_value:
            high-=1
        alist[0]=alist[high]



# 归并排序






if __name__ == '__main__':
    li = [64,21,22,9,5]
    # bubble_sort(li)
    # select_sort(li)
    # insert_sort(li)
    shell_sort(li)
    print(li)