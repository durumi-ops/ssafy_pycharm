'''
1부터 3까지 숫자에 대하여 [1,1,1]~...~[3,3,3]까지 구성해보자
'''

path = []
N = 3
def run(lev): # lev = 반복하게 만드는 횟수
    # 제약조건 설정: lev가 N번까지 도달하면 path 출력하고 종료(return)
    if lev == N:
        print(path)
        return
    for i in range(4):
        path.append(i)
        run(lev+1)
        path.pop()
run(0)
