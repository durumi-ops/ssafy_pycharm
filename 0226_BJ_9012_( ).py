# from collections import deque

T = int(input())


# arr를 돌면서 '('를 만나면 check리스트에 넣고, ')'를 만나면 check 리스트에서 '('를 하나씩 뺀다

arr = [input() for _ in range (T)]

for i in range(T):
    result = True
    check = []
    for chr in arr[i]:
        if chr=='(':
            check.append(chr)
        else:
            if check:
                check.pop()
            else:
                result = False
                break

    if result and not check: # result가 True이고, check 리스트가 비어있으면 -> YES 출
        # <and>를 써서 check리스트가 비어있는 경우에 대한 상황별 구분을 한다.
        print("YES")

    else:
        print("NO")



