# import sys
# sys.stdin = open('input.txt','r')

def fibo(num):
    if num <= 1:
        return num #1보다 작거나 같다면 그냥 그 값 자체로 돌려준다.

    return fibo(num-1)+fibo(num-2) # 최종적으로 나와야할 fibo 계산 식




N = int(input())

result = fibo(N)
print(result)





















def fibo(N):
    if N <= 1:
        return N
    return fibo(N-1)+fibo(N-2)