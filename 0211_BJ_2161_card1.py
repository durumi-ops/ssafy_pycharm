N = int(input())

# N까지의 카드리스트를 구성한다.

# 카드리스트의 개수가 1개가 남을 때까지-
    # 첫번째 숫자는 삭제하고 (-> trash 리스트에 저장하면서)
    # 다음 숫자는 맨 뒤로 넘기는 것을 반복한다.

card = list(range(1,N+1))
trash = []

while len(card) > 1:
    trash.append(card.pop(0))
    # card = [1,2,3,4]일때 -> trash = [1] // card=[2,3,4]
    # 삭제 완료
    card.append(card.pop(0))
    # card = [2,3,4] 에서 -> card.pop(0)=2이기 때문에 2를 지우고 // 다시 card리스트에 추가한다.
    # card = [3,4,2]

print(*trash,*card)

# N = int(input())
#
# cards = list(range(1, N+1))  # 1부터 N까지 리스트 만들기
# discarded = []               # 버린 카드 저장
#
# while len(cards) > 1:        # 카드가 1장 남을 때까지
#     discarded.append(cards.pop(0))  # 맨 앞 카드 버리기
#     cards.append(cards.pop(0))      # 그 다음 카드를 맨 뒤로 보내기
#
# print(*discarded)
# print(cards[0])