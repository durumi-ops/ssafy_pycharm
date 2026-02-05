#슬라이딩 윈도우

#연속된 3개 숫자의 합을 구하고, 합 중 가장 큰 합을 구하여라
arr= [20,32,16,25,36]


for start in range(len(arr)-2):
    total = 0
    for i in range(start,start+3):
        total += arr[i]
    print(total)

#-----------------------------------------------------------
#윈도우 개념으로 더하기
#연속된 K개 숫자의 합 중 가장 큰 합을 구하여라
arr = [20, 32, 16, 25, 36, 23, 42, 53, 63, 46]
#len(arr) = 10
k = 5
window = sum(arr[:k])
max_sum = window

for i in range(len(arr)-k):
    window = window - arr[i] + arr[i+k]
    if window > max_sum:
        max_sum = window

print(f'최대합: {max_sum}')