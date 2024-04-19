# ----------------------------------------------------------------------------
# D2[SWEA_1983] 조교의 성적 매기기
# ----------------------------------------------------------------------------
import sys
from collections import defaultdict
input = sys.stdin.readline

for t in range(1, int(input())+1):
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    # 학생수 n, 학점 알고싶은 학생 번호 k
    n, k = map(int, input().split())

    student = []

    for i in range(n):
        mid, last, homework = list(map(int, input().split()))
        total = mid * 0.35 + last * 0.45 + homework * 0.2
        student.append(total)
    
    # k번쨰 학생 총점
    k_score = student[k-1]
    student = sorted(student, reverse=True)
    
    # 해당 학점은 div 수 만큼 받음.
    div = n//10
    k_score = student.index(k_score)// div
    
    print("#{} {}".format(t, grade[k_score]))

# 요약
# 중간, 기말, 과제 순서 점수가 주어진다.
# 중간고사 (35%) + 기말고사 (45%)+ 과제 (20%)

# 풀이
# 학점은 n//10, 30명이면 하나의 학점은 3명 받을 수 있음.
# 따라서 해당 위치의 인덱스//div 하면 grade 인덱스에 맞는 학점을 부여받을수 있음.
