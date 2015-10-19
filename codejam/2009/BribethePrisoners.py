import itertools
def calcBribes(p,r,q):
    g=0
    for pr in q:
        p[pr-1]=0
        pointer=pr
        while(pointer < len(p) and p[pointer]!=0):
            g+=1
            pointer+=1
        pointer=pr-2
        while (pointer >=0 and p[pointer]!=0):
            g+=1
            pointer-=1
    return g
def solve(p,r,q):
    pers=itertools.permutations(r)
    m=999999999999
    for per in pers:
        pn=p[:]
        temp=calcBribes(pn,r,per)
        if m>temp:
            m=temp
    return m
    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(" ")
    p=range(1,int(line[0])+1) ; q = int(line[1])
    r=[int(x) for x in fin.readline().strip().split(" ")]
    fout.write("Case #"+str(case)+": "+str(solve(p,r,q))+"\n")