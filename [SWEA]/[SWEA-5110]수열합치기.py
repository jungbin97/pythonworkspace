# for test_case in range(1, int(input())+1):
#     N, M = map(int, input().split())    # N 수열의 길이 M 수열의 개수
#     # 합쳐질 수열 만들기
#     arr = [float('inf')] # 양의 무한대 inf (최댓값 구할때)
#     cnt = 0 


#     for _ in range(M):
#         # 개별 수열 a
#         a = list(map(int, input().split()))
#         for i in range(N*cnt+1):
#             if a[0] < arr[i]:
#                 arr[i:i] = a
#                 break
#         cnt += 1
#     print(arr[-11:-1][::-1])
# ------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
    
class SingLinkedList:
    def __init__(self):
        new_node = Node("head")
        self.head = new_node
        self.tail = new_node
        self.before = None
        self.current = None
        self.num_of_data = 0

    # # 연결 리스트가 비어있는지
    # def is_empty(self):
    #     return not bool(self.head)
    
    # 연결 리스트의 맨 뒤에 삽입
    def append(self, data):
        new_node = Node(data)   # 새 노드 생성
        self.tail.link = new_node
        self.tail = new_node 
        self.num_of_data += 1

    def first(self):
        if self.num_of_data == 0:
            return None
        self.before = self.head
        self.current = self.head.link
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.link
        if self.current == None:
            return None 
        return self.current.data 

    def insertlist(self, new_list):
        insert_num = new_list.first()
        num = self.first()

        for _ in range(self.num_of_data):
            if num > insert_num:
                self.before.link = new_list.head.link
                new_list.tail.link = self.current
                self.num_of_data += new_list.num_of_data
                break
            num = self.next()
        else: # 큰 숫자가 없는 경우 원래 linked list의 마지막으로 이동
            self.tail.link = new_list.head.link
            self.num_of_data += new_list.num_of_data

    # 결과 출력 함수
    def reusult(self):
        lst =[]
        num = self.first()
        for _ in range(self.num_of_data):
            lst.append(num)
            num = self.next()
        return " ".join(map(str, lst[-1:-11:-1]))

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())    # N 수열의 길이 M 수열의 개수

    seq1 = SingLinkedList()
    
    for i in map(int, input().split()):
        seq1.append(i)

    for _ in range(M-1):
        seq2 = SingLinkedList()
        for j in map(int, input().split()):
            seq2.append(j)
        seq1.insertlist(seq2)

    print("#{} {}".format(test_case, seq1.reusult()))