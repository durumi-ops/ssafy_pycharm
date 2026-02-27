import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
target = 1


for i in range(N):
    stack.append(arr[i])  # 일단 스택에 넣어준다

    while stack and stack[-1]==target:
        stack.pop()
        target+=1

if not stack:
    print("Nice")
else:
    print("Sad")






