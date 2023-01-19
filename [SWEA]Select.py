# 1번부터 k번째까지 작은 원소를 찾아 List 앞쪽으로 이동시키고, List의 k번째를 반환
# k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 함

def select(list, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]

list = [1, 3, 7, 100, 4, 55, 32, 17, 78, 99, 123]
select(list, 5)

# 선택 정렬 과정
def selectionSort(a):
    for i in range(0, len(a)- 1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
