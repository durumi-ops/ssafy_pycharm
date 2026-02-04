matrix = list(map(int,input().split()))
# 2 5 5 7 4 3

list = [0]*(max(matrix)+1)
#matrix 안의 (최댓값+1)개 만큼의 0이 담긴 list를 만든다.
#[0 0 0 0 0 0 0 0]

for num in matrix:
    list[num]+=1
#matrix에 담긴 숫자를 인덱스로 인식하고, 각 인덱스에 1만큼의 숫자를 더한다.
#[0 0 1 1 1 2 0 1]

for i in range(0,len(list)-1):
    list[i+1] += list[i]
#[0 0 1 2 3 5 5 6]

reverse_matrix = matrix[::-1]
# [3 4 7 5 5 2]

new_list = [0]*(max(matrix)+1)
for num in reverse_matrix:
    new_list[list[num]] = num
    list[num] -= 1


print(new_list)