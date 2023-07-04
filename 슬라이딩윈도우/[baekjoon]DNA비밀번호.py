# ----------------------------------------------------------------------------
# [baekjoon] DNA비밀번호(슬라이딩 윈도우, python)
# ----------------------------------------------------------------------------
import sys
s, p = map(int, sys.stdin.readline().split())
str = list(sys.stdin.readline().rstrip())
DNA = [0,0,0,0]
minNum = list(map(int, sys.stdin.readline().split()))   # A, C, G, T
start = 0
end = p
count = 0

def DNA_count(start, end):
    global count
    global DNA
    for i in range(start, end):
        if str[i] == "A":
            DNA[0] += 1
        elif str[i] == "C":
            DNA[1] += 1
        elif str[i] == "G":
            DNA[2] += 1
        elif str[i] == "T":
            DNA[3] += 1
    if (DNA[0] >= minNum[0]) and (DNA[1] >= minNum[1]) and (DNA[2] >= minNum[2]) and (DNA[3] >= minNum[3]):
        count += 1


DNA_count(start, end)

# 슬라이딩 윈도우 기법 사용
for i in range(end, s):
    if str[i] == "A":
        DNA[0] += 1
    elif str[i]== "C":
        DNA[1] += 1
    elif str[i] == "G":
        DNA[2] += 1
    elif str[i] == "T":
        DNA[3] += 1
if (DNA[0] >= minNum[0]) and (DNA[1] >= minNum[1]) and (DNA[2] >= minNum[2]) and (DNA[3] >= minNum[3]):
    count += 1
    
    if str[i-p] == "A":
        DNA[0] -= 1
    elif str[i-p] == "C":
        DNA[1] -= 1
    elif str[i-p] == "G":
        DNA[2] -= 1
    elif str[i-p] == "T":
        DNA[3] -= 1
if (DNA[0] >= minNum[0]) and (DNA[1] >= minNum[1]) and (DNA[2] >= minNum[2]) and (DNA[3] >= minNum[3]):
    count += 1
    
print(count)