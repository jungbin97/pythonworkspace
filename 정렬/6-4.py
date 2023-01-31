array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 한개인 경우 종료
        return
        
    pivot = start
    left = start+1
    right = end
    
    while left <= right:    # 2개의 리스트 일때 참
        # 피벗보다 큰데이터 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:  #left <= end 2개의 리스트 참
            left += 1
        # 피벗보다 작은데이터 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:  #right >= start버그??
            right -= 1
        if left > right: # 엇갈렸다면 작은데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰데이터 교체 
            array[right], array[left] = array[left], array[right]
    # 분할이후 왼쪽 리스트와 오른쪽 리스트 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)