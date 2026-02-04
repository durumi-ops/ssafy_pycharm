N = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)


for i in range(N): #여기서 scores는 리스트 형태이기 때문에 for num in scores라고 하면 인식하지 못함 (인덱스로 접근해야 함)
    scores[i] = scores[i] / max_score *100


print(sum(scores)/N)
# new_average = sum(scores) / N
# print(new_average)