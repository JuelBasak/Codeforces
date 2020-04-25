n = int(input())

words = []
for i in range(n):
    words.append(input())


abbs = []


for i in words:
    word = ''
    if len(i) <= 10:
        abbs.append(i)
        continue
    
    word = i[0] + str((len(i) - 2)) + i[-1]
    abbs.append(word)

for i in abbs:
    print(i)

