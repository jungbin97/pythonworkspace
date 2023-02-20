# --------------------- 단순 리스트 insert 함수로 구현 --------------------------
# for test_case in range(1, int(input())+1):
#     N, M, L = map(int, input().split())   # N 수열의 길이 M 추가횟수 L 출력할 인덱스 번호
#     arr = list(map(int, input().split()))

#     for _ in range(M):
#         idx, value = map(int, input().split())
#         arr.insert(idx, value)
#     print("#{} {}".format(test_case, arr[L]))
# ------------------------------------------------------------------------------
# 연결 리스트로 구현

class Node(object):
    def __init__(self, data, link=None):
        self.data = data
        self.link = link
    
class SingLinkedList(object):
    def __init__(self):
        self.head = None
    
    # 연결 리스트가 비어있는지
    def is_empty(self):
        return not bool(self.head)
    
    # 연결 리스트의 맨 뒤에 삽입
    def append(self, value):
        # 비었으면 head의 링크를 새노드의 주소로 바꾸기
        if self.is_empty():
            self.head = Node(value)
        # 링크가 None인(맨뒤) 노드 뒤에 삽입
        else:
            prev = self.head
            while prev.link != None:
                prev = prev.link
            newNode = Node(value)
            prev.link = newNode

    # 연결 리스트의 특정 위치에 삽입 
    def insert(self, index, value): 
        # 비었으면 head의 link를 새노드의 주소로 바꾸기 
        if self.is_empty(): self.head = Node(value)
        # 맨앞에 넣기 
        elif index == 0: 
            self.head = Node(value, self.head)
        # 중간에 넣기
        else:
            # 이전 노드(넣을 위치의 앞 노드)의 링크 구하기
            prev = self.head
            for i in range(index - 1):
                prev = prev.link
            # 새 노드 생성하기
            newNode = Node(value)
            # 이전 노드의 링크를 새 노드의 주소로 바꾸기
            tmp = prev.link
            prev.link = newNode
            # 새 노드의 링크를 이전 노드의 링크로 바꾸기
            newNode.link = tmp
    
    # 특정 위치의 원소 출력하기
    def printItem(self, index):
        target = self.head
        for i in range(index):
            target = target.link
        return target.data
        
    # 리스트 출력하기 (문제와 무관)
    def printList(self):
        target = self.head
        while target:
            if target.link != None:
                print(target.data, "->", end=" ")
                target = target.link
            else:
                print(target.data)
                target = target.link

for test_case in range(1, int(input())+1):
    sList = SingLinkedList()

    N, M, L = map(int, input().split())

    # 연결 리스트에 원소 추가하기
    sequence = list(map(int, input().split()))
    for s in sequence:
        sList.append(s)


    # 특정 위치에 숫자 추가하기
    for i in range(M):
        idx, num = map(int, input().split())
        sList.insert(idx, num)
    sList.printList()
    print("#{} {}".format(test_case, sList.printItem(L)))