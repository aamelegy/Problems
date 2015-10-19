def solve(p,k,f):
    f.sort()
    f.reverse()
    d=k
    pr=0
    for n in f:
        pr+=n*(d/k)
        d+=1
    return pr
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    p=int(line[0])
    k=int(line[1])
    f=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(p,k,f))+"\n")