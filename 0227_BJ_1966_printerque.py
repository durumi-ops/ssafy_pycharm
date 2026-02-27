import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    queue = list(map(int,input().split()))
    queue_set = [(b,a) for a,b in enumerate(queue,start=0)] # 숫자 먼저 받고 - idx 뒤에 받는 구조
    d_queue_set = deque(queue_set)
    print_list = []


    # print_list가 다 찰 때까지 시행할건데
    while d_queue_set:
        # 일단 제일 왼쪽(첫번째) 숫자 세트를 빼놓고 시작한다.
        current = d_queue_set.popleft()

        # 첫번째 숫자가 만약 나머지보다 작다면,
        if d_queue_set and current[0]<max(x[0] for x in d_queue_set): # d_queue_set에 숫자가 들어있는지도 확인해야함
            # d_queue_set 뒤로 보낸다.
            d_queue_set.append(current)
        # 첫 번째 숫자가 가장 큰 숫자라면
        else:
            # print_list에 해당 숫자 세트를 넣는다.
            print_list.append(current)

            if current[1]==M:
                print(len(print_list))
                break
