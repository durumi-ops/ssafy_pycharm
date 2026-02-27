import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()

for tc in range(N):
    n = list(map(int,input().split()))

    if n[0] == 1:
        q.appendleft(n[1])

    elif n[0]==2:
        q.append(n[1])

    elif n[0]==3:
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif n[0]==4:
        if q:
            print(q.pop())
        else:
            print(-1)

    elif n[0]==5:
        print(len(q))

    elif n[0]==6:
        if not q:
            print(1)
        else:
            print(0)

    elif n[0] ==7:
        if q:
            print(q[0])
        else:
            print(-1)









    elif n[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)




# command = [list(map(int,input().split())) for _ in range(N)]
# li = []
# q = deque(li)
#
# for i in range(N):
#     if command[i] == 3:
#         if not q:
#             print(-1)
#         else:
#             q.popleft()
#             print(q)
#
#     elif command[i] == 4:
#         if not q:
#             print(-1)
#         else:
#             q.pop()
#             print(q)
#
#     if command[i] == 5:
#         if not q:
#             print(-1)
#         else:
#             q.popleft()
#             print(q)