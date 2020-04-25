n, k = map(int, input().split())

c = list(map(int, input().split()))[:n+1]

base_score = c[k-1]

d = 0

for i in range(n):
    if c[i] > 0 and c[i] >= base_score:
        d += 1
        
print(d)

