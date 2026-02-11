import sys
sys.stdin = open('input.txt','r')



T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    que = list(map(int,input().split()))
    num = que[M]

    copy_list =[]

    while len(copy_list) < N:
        if max(que) > que[0]:
            p = que.pop(0) # 첫번째 숫자를 꺼내서
            que.append(p) # 삭제하고 뒤로 보낸다.

        else:
            p = que.pop(0) # 첫번째 숫자(중요도최상위) 꺼내서
            copy_list.append(p) #copy_list에 넣는다.

    print(copy_list.index(num) + 1)




# N = 4
# copy_list = []
# que = [1,2,3,4]
# while len(copy_list) < N:
#     while max(que) > que[0]:
#         que.pop(0)
#         que.append(que.pop(0))
#     copy_list.append(que[0])
#     que.remove(que[0])
#
#
# print(copy_list)

