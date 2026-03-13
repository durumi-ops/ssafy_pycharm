# 6개의 숫자를 입력받습니다.
cards = [0, 1, 7, 2, 7, 7]

# 1. 0부터 9까지 숫자가 몇 번 나왔는지 저장할 공간(바구니)을 만든다
counts = [0] * 11

# 2. 카드를 하나씩 확인하며 해당 숫자 바구니에 +1을 해줍니다.
for x in cards:
    counts[x] += 1

baby_gin_count = 0  # 완성된 세트(run 또는 triplet)의 개수



# i = 0
#
# # 3. 0번 바구니부터 9번 바구니까지 차례대로 검사합니다.
# while i < 10:
#     # [방법 A] 똑같은 숫자가 3개 이상인가? (Triplet)
#     if counts[i] >= 3:
#         counts[i] -= 3     # 3개를 사용함
#         baby_gin_count += 1
#         continue           # 똑같은 숫자가 또 있을 수 있으니 다시 검사
#
#     # [방법 B] 연속된 숫자가 3개 있는가? (Run)
#     # 예: i번, i+1번, i+2번 바구니에 사탕이 각각 1개 이상씩 있나?
#     if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
#         counts[i] -= 1
#         counts[i+1] -= 1
#         counts[i+2] -= 1
#         baby_gin_count += 1
#         continue           # 연속된 숫자가 또 있을 수 있으니 다시 검사
#
#     i += 1  # 다음 숫자로 넘어감
#
# # 4. 최종 결과 확인
# if baby_gin_count == 2:
#     print("Baby-gin입니다!")
# else:
#     print("아쉽네요, 아닙니다.")