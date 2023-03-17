def createQueue(N):
    # 크기 N인 1차원 리스트 생성
    arr = [0 for _ in range(N)]
    front = -1
    rear = -1
    print(arr)
    return arr, front, rear

def enQueue(arr, item, rear):
    if isFull(arr, rear):
        print("Queue_Full")
    else:
        rear += 1
        arr[rear] = item
    print(arr)
    return rear

def deQueue(arr, front):
    if isEmpty(front):
        print("Queue_Empty")
    else:
        front += 1
        return arr[front]
    print(arr)

def isEmpty(front):
    return front == rear

def isFull(arr, rear):
    return rear == len(arr) - 1

def Qpeek(arr, front):
    if isEmpty(front):
        print("Queue_Empty")
    else:
        return arr[front + 1]

arr, front, rear = createQueue(3)
rear = enQueue(arr, 'A', rear)
rear = enQueue(arr, 'B', rear)
deQueue(arr, front)
deQueue(arr, front)