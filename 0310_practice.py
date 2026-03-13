arr = [1,2,3,4,5]

# 순서대로 출력한 다음에

# 시작점: 0번째 index
# 종료지점: 4번째 index
#


def cal(i):
    if i==4:
        print(arr[i])
        return

    print(arr[i])
    cal(i+1)
    print(arr[i])




cal(0)