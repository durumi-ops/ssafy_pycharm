S =input()
num = -1
arr = [-1]*26 #미리 -1으로 이루어진 리스트를 만든다.



for i in S: #입력받은 문자열 S에 대하여,
    num += 1 # num = 입력받은 문자의 인덱스 하나씩 입력받을 때마다 1을 더한다 (각 문자열의 위치를 인덱스로 파악하기 위함 - 예: apple에서 a=0,p=1,l=3,e=4)
    loc = ord(i)-97 # loc = 알파벳 문자열의 위치 (아스키코드 활용)
    if arr[loc]==-1: #만약 처음 등장하는 문자라면
        arr[loc] = num #해당 위치의 -1을 num으로 바꾼다. (= 중복으로 등장하는 문자에 대해 첫번째 등장하는 문자 기준으로 인덱스를 인식한다)


for num in range(len(arr)):
    print(arr[num],end=' ')