import sys
input=sys.stdin.readline

t = int(input())
p=[0,1,1,1,2,2]+[0]*95
for i in range(6,101):
    p[i]=p[i-1]+p[i-5]
for _ in range(t):
    n=int(input())
    print(p[n])