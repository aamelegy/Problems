def solve(c,p):
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]+p[j]==c:
                return str(i+1)+" "+str(j+1)
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    c=int(fin.readline().strip())
    l=int(fin.readline().strip())
    p= [int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(c,p))+"\n")