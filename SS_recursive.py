'''피보나치 수열 만들기

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
'''

'''1부터 N까지 합 구하기
def sum_all(n):
    if n == 1:
        return 1

    return n+sum_all(n-1)

print(sum_all(10))
'''

'''문자열 거꾸로 출력
def reverse_string(s):
    if len(s)<=1:   # 글자가 하나라면
        return s    # 그 상태 그대로 출력한다.
    return s[-1]+reverse_string(s[:-1])
    # 맨 마지막 글자 + 마지막 전까지 reverse

print(reverse_string('python'))
'''

'''memoization
def fibo(n):
    if n >= 2 and memo[n]==0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


# n에 대한 입력값을 받는다
n = int(input())

#0번째 인덱스부터 시작할거니까 N+1을 곱해준다.
memo = [0]*(n+1)

# 미리 연산값 저장해두기 위한 memo list
memo[0] = 0 # 0번째는 0
memo[1] = 1 # 1번째는 1

print(fibo(n))
'''