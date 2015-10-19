def flows(i,j,basin):
    min=9999
    min_index=True
    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if di+i>0 and di+i<h and dj+j >0 and dj+j<w and basin[di+i][dj+j][0]<basin[i][j][0] and basin[di+i][dj+j][0] <min:
            min_index=di+i,dj+j
            min=basin[di+i][dj+j][0]
    return min_index        

def solve(h,w,basin):
    lb=97
    stack=[]
    for i in range (h):
        for j in range(w):
            n=i,j
            stack.append(n)
            while (n!=True ):
                if basin[n[0]][n[1]][1]!='-1':
                    stack.append(True)
                    break
                n=flows(n[0],n[1],basin)
                stack.append(n)
            stack.pop()
            if len(stack)>0:
                temp=stack.pop()
                if basin[temp[0]][temp[1]][1]!='-1':
                    label=basin[temp[0]][temp[1]][1]
                else:
                    label=chr(lb)
                    lb+=1
                basin[temp[0]][temp[1]][1]=label
                while(len(stack)>0):
                    temp=stack.pop()
                    basin[temp[0]][temp[1]][1]=label
    res=''
    for row in basin:
        for col in row:
            res+=col[1]
            res+=' '
        res=res.strip()
        res+='\n'
    return res.strip()

fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    h,w=int(line[0]),int(line[1])
    basin=[]
    for x in range(h):
        basin.append([[int(x),'-1'] for x in fin.readline().strip().split(' ')])
    fout.write("Case #"+str(case)+": "+"\n"+str(solve(h,w,basin))+"\n")