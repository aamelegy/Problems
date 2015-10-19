#small
import itertools
def solve(k,s):
    per=list(itertools.permutations([x for x in range(0,k)]))
    mi=999999999
    for p in per:
        last='vbxxs'
        c=0
        for i in range(len(s)/k):
            for j in p :
                if s[i*k+j]!=last:
                    c+=1
                    last=s[i*k+j]
        mi = min(mi,c)
    return mi
                    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    k=int(fin.readline().strip())
    s=fin.readline().strip()
    fout.write("Case #"+str(case)+": "+str(solve(k,s))+"\n")