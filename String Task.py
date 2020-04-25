s = input()
w = ''

for i in s:
    if i == 'A' or i == 'O' or i == 'Y' or i == 'E' or i == 'U' or i == 'I' or i == 'a' or i == 'o' or i == 'y' or i == 'e' or i == 'u' or i == 'i':
        continue
    
    elif ord(i) >= 65 and ord(i) <= 90:
        i = chr(ord(i) + 32)
    
    w = w + '.' + i

print(w)
    
    
    
