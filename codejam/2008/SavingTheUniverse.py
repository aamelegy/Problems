def solve(es,qs):
    eset=set(es)
    sw=0
    for q in qs:
        if q in eset:
            eset.remove(q)
        if len(eset)==0:
            eset=set(es)
            eset.remove(q)
            sw+=1
    return sw
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    e=int(fin.readline().strip())
    engines=[]
    for engine in range(e):
        engines.append(fin.readline().strip())
    qs=int(fin.readline().strip())
    querys=[]
    for query in range(qs):
        querys.append(fin.readline().strip())
    fout.write("Case #"+str(case)+": "+str(solve(engines,querys))+"\n")