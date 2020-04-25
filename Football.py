players = input()
count = 1
flag = 'NO'

for i in range(len(players) - 1):
    if players[i] == players[i + 1]:
        count += 1
        if count >= 7:
            flag = 'YES'
            break
    else:
        count = 1

print(flag)
