# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _reserve = sorted(_reserve)
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)
# -------------------- testcase 일부 실패 --------------------
#  _reserve 정렬 필요
# ------------------------------------------------------------
def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    for i in _lost:
        if i-1 in _reserve:
            _reserve.remove(i-1)
        elif i+1 in _reserve:
            _reserve.remove(i+1)
        else: 
            n-=1
    return n

print(solution(5, [2,4], [1,3,5]))
# ------------------- testcase 17,18,19,20,25 실패 ----------
#  i+1 부터 체크하면 안됨!(그리디 이기 떄문에 앞전에있는학생은 
#  받을 수 없는 상태가 됨) 
# ------------------------------------------------------------