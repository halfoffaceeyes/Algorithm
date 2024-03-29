dr=[0,1,0,-1]
dc=[1,0,-1,0]
def solution(grid):
    answer = []
    leng_row=len(grid)
    leng_col=len(grid[0])
    set_dir=set()
    for row in range(leng_row):
        for col in range(leng_col):
            for i in range(4):
                if not (row,col,i) in set_dir:
                    res=go(grid,row,col,i,i,set_dir,leng_row,leng_col,row,col)
                    set_dir.add((row,col,i))
                    if res:
                        answer.append(res)
    answer.sort()
    return answer
def go(grid,row,col,di_now,di_depart,set_dir,leng_row,leng_col,arow,acol):
    st=[(row,col,di_now,0)]
    while st:
        rr,cc,di,cnt=st.pop()
        state=grid[rr][cc]
        if state=='L':
            di-=1
            di%=4
        elif state=="R":
            di+=1
            di%=4
        r=(rr+dr[di])%leng_row
        c=(cc+dc[di])%leng_col
        if (r,c,di) in set_dir:
            return
        else:
            set_dir.add((r,c,di))
        if r==arow and c==acol and di==di_depart:
            return cnt+1
        st.append((r,c,di,cnt+1))

    
    