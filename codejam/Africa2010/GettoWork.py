from sets import Set
def solve(em,t):
    cr=[]
    towns=[int(x) for x in em.keys()]
    list.sort(towns)
    for to in towns:
        cars=0
        ps=0
        es=em[to]
        list.sort(es)
        list.reverse(es)
        if str(t)==str(to):
            cr.append(0)
            continue
        for e in es:
            ps+=e
            if e>=1:
                cars+=1
            if ps>=len(es):
                break
        if ps<len(es):
            return "IMPOSSIBLE"
        else:
            cr.append(cars)
    return ' '.join([str(x) for x in cr])
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    n=int(line[0]) ; t=int(line[1]) 
    e=int(fin.readline().strip())
    em=dict()
    for nt in range(1,n+1):
        em[nt]=[]
    for i in range(e):
        line=fin.readline().strip().split(' ')
        em[int(line[0])].append(int(line[1]))
    fout.write("Case #"+str(case)+": "+str(solve(em,t))+"\n")