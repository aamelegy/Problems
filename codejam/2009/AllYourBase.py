def solve(n):
    s=0
    j=dict()
    for ch in n :
        j[ch]=-1
    b=max(len(j),2)
    h=len(n)-1
    s+=1*(b**h)
    j[n[0]]=1
    d=0
    for i in range(1,len(n)):
        h=len(n)-i-1
        if j[n[i]]!=-1:
            x=j[n[i]]
        else:
            x=d
            j[n[i]]=d
            d+=1
            if d==1:
                d+=1
        s+=x*(b**h)
    return s
    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    n=fin.readline().strip()
    fout.write("Case #"+str(case)+": "+str(solve(n))+"\n")