def solve(g,ng,n,m):
    for i in range(n):
        sh=max(g[i])
        for j in range(m):
            if ng[i][j]>sh:
                ng[i][j]=sh
    for j in range(m):
        sh=max([g[i][j] for i in range(n)])
        for i in range(n):
            if ng[i][j]>sh:
                ng[i][j]=sh
    for i in range(n):
        for j in range(m):
            if ng[i][j]!=g[i][j]:
                return 'NO'
    return 'YES'
                    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    g=[] ; ng=[]
    line=fin.readline().strip().split(' ')
    n=int(line[0]); m=int(line[1])
    for i in range(n):
        g.append([int(x) for x in fin.readline().strip().split(' ')])
        ng.append([100]*m)
    fout.write("Case #"+str(case)+": "+str(solve(g,ng,n,m))+"\n")