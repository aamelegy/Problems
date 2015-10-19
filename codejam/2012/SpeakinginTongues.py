def solve (l):
    ret=[]
    for i in range(len(l)):
        ret.append(o[c.index(l[i])])
    return ''.join(ret)
        


c='qzejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepky mveddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
o='zqour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    l=fin.readline().strip()
    fout.write("Case #"+str(case)+": "+str(solve(l))+"\n")