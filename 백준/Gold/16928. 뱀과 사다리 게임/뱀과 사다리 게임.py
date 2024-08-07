import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
ladder = {a:b for a,b in [map(int,input().split()) for _ in range(n)]}

snake = {a:b for a,b in [map(int,input().split()) for _ in range(m)]}
res=[200]*101
q=deque([(1,0)])
def bfs():
    while q:
        now, cnt = q.popleft()
        if now ==100:
            res[100]=min(res[100],cnt)
        elif now in ladder:
            go = ladder[now]
            if res[go]>cnt:
                res[go]=cnt
                q.append((go,cnt))
        elif now in snake:
            go = snake[now]
            if res[go]>cnt:
                res[go]=cnt
                q.append((go,cnt))
        else:
            for i in range(6,0,-1):
                go=now +i
                if go<=100 and res[go]>cnt:
                    res[go]=cnt+1
                    q.append((go,cnt+1))
bfs()
print(res[100])