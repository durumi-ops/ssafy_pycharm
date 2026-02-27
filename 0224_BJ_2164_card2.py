from collections import deque


N = int(input())
card = list(range(1,N+1))

queue=deque(card)

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())   # 이 부분 중요!!!!!

print(*list(queue))