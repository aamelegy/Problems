from sets import Set
def solve(g):
    co=Set()
    for gu in g:
        if gu in co :
            co.remove(gu)
        else:
            co.add(gu)
    for v in co:
        return str(v)
        
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    fin.readline().strip()
    g=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(g))+"\n")