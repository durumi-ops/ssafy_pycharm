# 문제: 3*3 배열을 만들되,
# 1 2 3
# 6 5 4
# 7 8 9
# 위와 같은 방법으로 출력되도록 만들어라.

N = 3
arr = [[0]*N for _ in range(N)]
# print(arr)

num = 0
x = 0
y = 0
for i in range(N):
    x = i
    if i%2 == 0:
        for j in range(N):
            y = j
            num += 1
            arr[i][j] = num

    else:
        for j in range(N):
            y = j
            num += 1
            arr[i][N - j - 1] = num

print(arr)
