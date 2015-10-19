def solve(s):
    si=[int(s[x]) for x in range (len(s))]
    t=99
    f=True
    for i in range(len(si)):
        if si[i]<=t:
            t=si[i]
        else:
            f=False
    if f:
        si.sort()
        re=''.join([str(x) for x in si])
        c=0
        for ch in re:
            if ch=="0":
                c+=1
        re=re[c]+re[0:c]+re[c+1::]
        return ''.join(re[0]+"0"+re[1::])
    last=-1
    p=len(s)-1
    while int(s[p])>=last and p>-1:
        last=int(s[p])
        p-=1
    a=s[p]
    for i in range(len(s)-1,p,-1):
        if s[i]>s[p]:
            b=s[i]
            break
    c=[int(x) for x in s[p+1:i]+s[p]+s[i+1::]]
    c.sort()
    c=[str(x) for x in c]
    c=''.join(c)
    return s[0:p]+s[i]+c
    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    s=fin.readline().strip()
    fout.write("Case #"+str(case)+": "+str(solve(s))+"\n")