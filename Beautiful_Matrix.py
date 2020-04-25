mylist = []

for i in range(5):
    mylist.append([int(i) for i in input().split()])


target_row = 2
target_col = 2

index = 0

for i in mylist:
    if 1 in i:
        temp_row = index
        for j in range(len(i)):
            if i[j] == 1:
                temp_col = j
    index += 1

moves = abs(target_row - temp_row) + abs(target_col - temp_col)

print(moves)
