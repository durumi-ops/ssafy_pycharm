T = int(input())
word=[]
for _ in range (T):
    word.append(input().strip()) #strip() : 입력받은 문자 앞뒤 공백 제거


for i in range(T):
    if word[i] == word[i][::-1]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
