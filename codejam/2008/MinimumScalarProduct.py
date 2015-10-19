def solve(v1,v2):
    v1.sort()
    v2.sort()
    v2.reverse()
    pro=0
    for i in range(len(v1)):
        pro+=v1[i]*v2[i]
    return pro
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    fin.readline().strip()
    v1=[int(x) for x in fin.readline().strip().split(' ')]
    v2=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(v1,v2))+"\n")