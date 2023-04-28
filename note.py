import heapq
q = []

for i in range(3):
    heapq.heappush(q, (1, 2))


print(heapq.heappop(q)[1])