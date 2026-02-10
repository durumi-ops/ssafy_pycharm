def fibo(num):
    if num <= 1:
        return num

    if memo.get(num): #계산한적이 있다면
        return memo[num] #기존 기록된 값을 return


    #한 번이라도 연산했다면, 딕셔너리 에 기록
    memo[num] = fibo(num-1) + fibo(num-2)
    return memo[num]

N = int(input())
memo = {}
result = fibo(N)
print(result)