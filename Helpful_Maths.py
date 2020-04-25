num = input().split('+')

num.sort()

mylist = ''
for i in num:
    mylist += i + '+'

print(mylist[:-1])
