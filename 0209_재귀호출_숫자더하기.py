#1부터 10까지 더하는 재귀함수 식

def cal(num):
    global cnt

    if num>10:
        return

    cnt += num
    cal(num+1)

cnt = 0
cal(1)

