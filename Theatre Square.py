l, b, a = map(int, input().split())

def fun(b, a):
    d = b // a
    c = b % a
    
    if c != 0:
        d += 1
    return d
        
v1 = fun(b, a)
v2 = fun(l, a)
print(v1 * v2)
    