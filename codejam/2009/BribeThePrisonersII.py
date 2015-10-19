mc=dict()
def solve(r,s,e):
    if (s,e) in mc:
        return mc[(s,e)]
    if s>=e:
        return 0
    r_c=0
    for pr in r:
        if pr >=s and pr<=e:
            tmp=(e-s)+solve(r,s,pr-1)+solve(r,pr+1,e)
            if tmp < r_c or r_c==0:r_c=tmp
    mc[(s,e)]=r_c        
    return r_c
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    mc=dict()
    line=fin.readline().strip().split(" ")
    p=range(1,int(line[0])+1) ; q = int(line[1])
    r=[int(x)-1 for x in fin.readline().strip().split(" ")]
    fout.write("Case #"+str(case)+": "+str(solve(r,0,len(p)-1))+"\n")