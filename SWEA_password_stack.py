# T= 10
# for tc in range(1,T+1):
#     n, s = input().split()
#     stack = []
#
#     for ch in s:
#         if stack and stack[-1]==ch: #stack이 비어있지 않고 + 마지막 문자가 ch와 같을 때
#             stack.pop() #해당 문자 return하고 리스트에서 지운다 (=pop)
#
#         else:
#             stack.append(ch) # 그렇지 않으면 그냥 채우기
#
#     print(f'#{tc}',end=' ')
#     print(''.join(stack))

import sys
sys.stdin = open('input.txt','r')


# for tc in range(1,11):
#     N, S = input().split()
#     stack = [] #비어있는 stack 리스트 만들기
#     for ch in S:
#         if stack and stack[-1]==ch:
#             stack.pop()
#         else:
#             stack.append(ch)
#
#     print(f'#{tc}', end=' ')
#     print(''.join(stack))



for tc in range(1,11):
    N, S = input().split()
    stack = [] #비어있는 stack 리스트 만들기
    for ch in S:
        #stack이 비어있으면, 그냥 숫자를 stack에 넣어준다.
        if len(stack) == 0:
            stack.append(ch)

        #stack의 마지막 데이터아 현재 숫자를 비교한다.
        # - 같다면 stack의 마지막 숫자를 제거
        # - 다르다면 stack에 숫자를 추가
        else:
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
    print(f'#{tc} {"".join(stack)}') #밖에가 ''이면 안에는 "" 해야한다 (겹치면 오류남)