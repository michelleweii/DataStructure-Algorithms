# 二分查找

# 要求序列有序

def binary_search(alsit,item):
    """二分查找，递归"""
    n = len(alsit)
    if n>0:
        mid = n//2
        if alsit[mid] == item:
            return True
        elif item<alsit[mid]:
            return binary_search(alsit[:mid],item)
        else:
            return binary_search(alsit[mid+1:],item)
    return False

def binary_search_2(alist,item):
    """二分查找，非递归"""
    n = len(alist)
    first = 0
    last = n-1
    while first<=last:
        mid = (first + last) // 2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            last=mid-1
        else:
            first=mid+1
    return False

if __name__ == '__main__':
    li = [17,20,26,31,44,54]
    print(binary_search(li,55))
    print(binary_search(li,17))
    print(binary_search_2(li,55))
    print(binary_search_2(li,17))