#1. 집이 어떻게 연결되었는지 적어둔 지도
viliage_map = {
    1: [2, 3], # 1번 집은 2번, 3번과 연결
    2: [4, 5], # 2번 집은 4번, 5번과 연결
    3: [],     # 3번 집은 연결된 곳 없음
    4: [],     # 4번 집은 연결된 곳 없음
    5: []      # 5번 집은 연결된 곳 없음
}

#2. 이미 방문한 곳 다시 안가기 위한 장치
stamp = []

def visit_house(current):
    # current(현재위치)가 이전에 방문한 적이 있다면
    if current in stamp:
        return  # 아무것도 안하고 원래 있던 집으로 돌아감

    # current(현재위치)가 처음 방문한 곳이라면
    else:
        stamp.append(current)
        print(f'{current}번 집 방문! 도장을 찍었습니다.')

    # 현재 집과 연결된 다른 집을 확인해본다.
    for next_house in village_map[current]:
        visit_house(next_house)  # 재귀함수 구현

    # for문 특징: 꺼낼 물건(next_house)가 없으면 -> 안쪽으로 들어가지 않고 for문을 그냥 통과함.
    # 따라서, 1->2->4까지 갔을 때 4에 대해서 for문이 발생하지 않고 바로 이전 for문인 2로 간다. (2->5)
    # return 되어 바로 이전 단계인 2에 대한 for문 상태로 회귀






