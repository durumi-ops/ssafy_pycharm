'''
완전탐색 문제2. 연속 3장의 트럼프 카드
A,J,Q,K 네종류 카드들이 충분히 있음
이중 5장 카드를 뽑아 나열

같은 종류 카드가 세장 연속으로 나오는 경우의 수는?
'''

'''
card = ['A','J','Q','K']
path= []
cnt = 0

# 각각의 카드 배열에 대하여 세 장 연속의 카드가 있는지 여부 파악하는 함수
def cont_three():
    if card[0]==card[1]==card[2]:
        return True
    if card[1]==card[2]==card[3]:
        return True
    if card[2]==card[3]==card[4]:
        return True
    return False

# 만들 수 있는 트럼프 카드 배열 만드는 방법
def permu(lev):

    if lev == 5:
        print(path)
        return

    for i in range(4):
        path.append(card[i])
        permu(lev+1)
        path.pop()


permu(0)
'''
################################################

card = ['A','J','Q','K']
path= []
result = 0

# 카드 5장을 뽑는다
# 한 번의 선택 -> 4가지 경우의 수

# 연속하는 카드 3장이 있는지 확인하기 위한 함수
def count_three():
    if card[0]==card[1]==card[2]:
        return True
    if card[1]==card[2]==card[3]:
        return True
    if card[2]==card[3]==card[4]:
        return True
    return False


def recur(cnt):
    global result

    if cnt == 5:
        # 만약 3장이 연속되면 result += 1
        if count_three():
            print(*path)
            result += 1
        return

    for i in range(4):
        path.append(card[i])
        recur(cnt+1)
        path.pop()      # 나뭇가지 도식화에서 봤을 때 하나 상위로 가야하니까.


recur(0)
print(result)

###################### 강사님 정답 코드 ###########################
'''
cards = ['A', 'J', 'Q', 'K']
path = []
result = 0


def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False


# 카드 5장을 뽑는다
# 한 번의 선택 -> 4가지의 경우의 수

def recur(cnt):
    global result

    if cnt == 5:  # 5장을 골랐다
        # 만약 3장이 연속되면 result += 1
        if count_three():
            print(*path)
            result += 1
        return

    # 카드 4개 중 하나를 선택
    for i in range(4):
        path.append(cards[i])
        recur(cnt + 1)
        path.pop()

    # # A 선택
    # path.append(cards[0])
    # recur(cnt + 1)
    # path.pop()
    #
    # # J 선택
    # path.append(cards[1])
    # recur(cnt + 1)
    # path.pop()
    #
    # # Q 선택
    # path.append(cards[2])
    # recur(cnt + 1)
    # path.pop()
    #
    # # K 선택
    # path.append(cards[3])
    # recur(cnt + 1)
    # path.pop()


recur(0)
print(result)
'''