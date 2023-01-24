# 큰 수의 법칙
# N 배열의 크기, M 숫자 더해지는 횟수, K 한번에 중복할 수 있는 횟수

n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬하기

first = data[n-1]   #가장 큰 수
second = data[n-2]  #두번째로 큰 수

#가장 큰수 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += (count) * first   #가장 큰 수 더하기
result += (m-count) * second    #두 번쨰로 큰 수 더하기

print(result)

""" result = 0

while True :
    for i in range(k):  #가장 큰 수를 k번 더하기
        if m == 0:  #m이 0이라면 반복문 탈출
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second #두 번쨰로 큰 수를 한 번 더하기
    m-=1

print(result) """