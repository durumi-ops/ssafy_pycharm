'''
게임 개발자 최 프로님은, 3D 엔진을 개발하는 업무를 맡았습니다.
3D 엔진을 개발하기 위해서는 Root 값을 구하는 경우가 많습니다.

회사에서 사용하는 Math Library의 sqrt 함수의 성능이 좋지 않아,
Root 값을 계산하는 프로그램을 직접 개발하기로 결정하였습니다.


Math Library 를 사용하지 않고,
Root 값의 정수부를 O(log N) 속도로 구해주는 프로그램을 작성해 주세요.



예를들어,
16의 root값은 4이며, 정수값은 4입니다.
17의 root 값은 4.xxx이며, 정수값은 4입니다.
25의 root 값은 5.xxx이며, 정수값은 5입니다.
35의 root 값은 5.xxx이며, 정수값은 5입니다.
'''

import sys
sys.stdin = open('input.txt','r')


N = int(input())
for tc in range(1, N+1):

    num = int(input())
    # 범위 정하기
    low = 0
    high = num
    answer = 0 # 일단 초기값은 0으로 임시 세팅

    # 이진 탐색
    while low <= high:
        # 일단 임시로 mid 값을 답으로 세팅
        mid = (low+high)//2

        # 해당 mid를 제곱해보고 확인하기
        if mid*mid <= num:
            answer = mid
            # 하나 더 큰 숫자도 체크해보기 (오른쪽 탐색)
            low = mid + 1

        # 만약 제곱했는데 N을 넘긴다면 -> 정답보다 큰 숫자이므로 더 작은 쪽으로 탐색해야 함
        else:
            high = mid-1

    print(f'#{tc} {answer}')

