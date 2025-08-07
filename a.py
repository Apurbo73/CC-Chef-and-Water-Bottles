import math
n= int(input())
for _ in range (n):
    a,b,c= map(int, input().split())
    if b>c:
        print(0)
    else:
        d=int(c/b)
        if d>=a:
            print(a)
        else:
            print(d)