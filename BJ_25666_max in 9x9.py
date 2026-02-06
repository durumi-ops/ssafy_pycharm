arr = [list(map(int,input().split())) for _ in range(9)]

max = 0
x=0
y=0
for r in range(9):
    for c in range(9):
        if arr[r][c]>max:
            max = arr[r][c]
            x = c
            y = r

print(max)
print((y+1),(x+1))