# 주사위 N개를 던졌을 때 나올 수 있는 모든 경우의 수
# N=3



# 시작점: 첫번째 던졌을 때
# 종료지점: n번째 던졌을 때
# 다음 재귀 호출: 1~6 6가지


n=3
arr=[]


def cal(n, subset, prev):
    if n==3:
        print(subset)
        return

    for i in range(prev,7):
        cal(n + 1, subset +[i], i)




cal(0,[],1)
