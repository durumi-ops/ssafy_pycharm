# 아래 내용 추가해야 백준에서 시간초과 안뜸....
import sys  # 1. sys 모듈을 불러옵니다.
input = sys.stdin.readline  # 2. input 함수를 더 빠른 readline으로 교체합니다.


N = int(input())
# 이렇게 하니까 시간초과 뜸 -> 꼭 request_list 로 입력값을 받지 않아도 된다.!!!!!
# request_list = [list(input().split()) for _ in range(N)]
stack_list = []


for _ in range(N):
    command = input().split()  # 공백으로 숫자를 구분해서 입력값을 받는다.
    if command[0]=='1':
        stack_list.append(command[1])

    #elif를 쓰지 않으면 시간초과 난다. (안그러면 해당 숫자가 아님에도 불구하고 다 일일이 확인해서 시간초과 뜸)
    elif command[0]=='2':
        if not stack_list:
            print(-1)
        else:
            print(stack_list.pop())

    elif command[0]=='3':
        print(len(stack_list))

    elif command[0]=='4':
        if stack_list:
            print(0)
        else:
            print(1)

    elif command[0] == '5':
        if stack_list:
            print(stack_list[-1])
        else:
            print(-1)



############################### 오답노트 #############################
'''request_list = [list(input().split()) for _ in range(N)]
stack_list = []


for i in range(N):
    if len(request_list[i])>1:
        stack_list.append(request_list[i][1])

    else:
        if request_list[i][0]=='2':
            if not stack_list:
                print(-1)
            else:
                print(stack_list.pop())

        if request_list[i][0]=='3':
            print(len(stack_list))

        if request_list[i][0]=='4':
            if stack_list:
                print(0)
            else:
                print(1)

        if request_list[i][0] == '5':
            if stack_list:
                print(stack_list[-1])
            else:
                print(-1)
'''
