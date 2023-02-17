# -----------------------아이디어 -------------------------------
# 알고리즘 스킬보다 사고력이 중요한 문제 완전탐색으로 접근해서
# 2차 리스트 요소를 reverse해서 풀려다가 실패함.
# 모든 명함의 두 변중 큰쪽을 가로로 눕혀 높이h를 두변중 작은 것들 중 가장 큰 변으로 구성

def solution(sizes):
   return max(max(x) for x in sizes) * max(min(y) for y in sizes)
    
# --------------------다른 풀이-------------------------------
#  람다식 이용

lambda sizes : max(sum(sizes, [])) * max(min(y) for y in sizes)