N,X = map(int,input().split())
arr = list(map(int,input().split()))

window = sum(arr[:x])
max_window = window
max_day = 1

for i in range(N-X):
    window=window-arr[i]+arr[i+X]

    #1. 최대 window 갱신
    if window > max_window:
        max_window = window
        max_day = 1

    #2. 최대값이 동일하면 max_day += 1
    elif window == max_window:
        max_day +=1


if max_window == 0:
    print("SAD")
else:
    print(max_window)
    print(max_day)
