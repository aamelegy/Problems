#wrong
def solve(n,k,p):
    d=[]
    for i in range(n-1):
        t=[]
        for j in range(n):
            if i==j:
                continue
            v=abs(p[i][1]-p[j][1])
            h=abs(p[i][0]-p[j][0])
            t.append(max(v,h))
        t.sort();  d.append(t[0])
    d.sort();d.reverse()
    if k<n:
        return d[k]
    else:
        return 0
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    n=int(line[0]);k=int(line[1])
    p=[]
    for i in range(n):
        l=fin.readline().strip().split(' ')
        p.append((int(l[0]),int(l[1])))
    fout.write("Case #"+str(case)+": "+str(solve(n,k,p))+"\n")