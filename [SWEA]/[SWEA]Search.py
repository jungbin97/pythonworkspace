# 완전 탐색
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        
# 이진탐색1
def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end - start)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False

# 이진탐색2 (재귀로 구현)
def binarySearch2(a, low, high, key):
    if low > high: # 검색 실패시
        return True
    else:
        middle = (low + high) //2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle -1, key)
        elif key > a[middle]:
            return binarySearch2(a, middle+1, high, key)
