def binarySearch(page, key):
    start = 1
    end = page
    count = 0

    while start <= end:
        middle = int((start+end)/2)
        if middle == key:
            return count
        elif key < middle:
            end = middle
            count +=1
        else:
            start = middle
            count += 1

T = int(input())

for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())   # P 전체 쪽 수, Pa A가 찾을 쪽 수, Pb B가 찾을 쪽 수

    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)
    
    if A<B:
        result = 'A'
    elif A>B:
        result = 'B'
    else:
        result = 0
        
    print("#%d %s" %(test_case, result)) 