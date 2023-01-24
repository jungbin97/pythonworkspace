'''
n queen (백트래킹, DFS)
- N X N 체스보드에 N개의 퀸을 배치
- 같은 행, 열, 대각선에 다른 퀸 놓을 수 없음
'''

#N 입력 받기
n = int(input())

checknode(node v):
    node u
    if(promising(v)
       if(v에 해답 있으면):
           해답 출력
       else:
           for(v 모든 자식 노드 u에 대해서):
               checknode(u)