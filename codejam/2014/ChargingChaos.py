def xor(a,b):
    tmp=""
    for i in range(len(a)):
        if a[i]==b[i]:
            tmp+="0"
        else:
            tmp+="1"
    return tmp
        
def solve (init,req):
    cand=dict()
    for i in range(len(init)):
        for j in range(len(req)):
            x=xor(init[i],req[j])
            if x in cand:
                cand[x]+=1
            else:
                cand[x]=1
    mi=9999999            
    for key in cand:
        if cand[key]==len(init):
            mi=min(key.count("1"),mi)
    if mi==9999999 :
        return "NOT POSSIBLE"
    return mi
        

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=[int(x) for x in fin.readline().strip().split(' ')]
    n=line[0] ; l=line[1] 
    init=fin.readline().strip().split(' ')
    req=fin.readline().strip().split(' ')
    fout.write("Case #"+str(case)+": "+str(solve(init,req))+"\n")