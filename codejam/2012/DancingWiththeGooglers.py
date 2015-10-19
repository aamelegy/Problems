def solve (s,p,t):
    c=0
    for i in range(len(t)):
        b=t[i]/3 ; a=t[i]%3
        if p-b<=0 :
            c+=1
        elif p-b==1 and a>=1 :
            c+=1
        elif p-b==1 and a==0 and s>0 and b>0:
            c+=1 
            s-=1
        elif p-b==2 and a==2 and s>0:
            c+=1
            s-=1
    return c
            
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    l=fin.readline().strip().split(' ')
    n=int(l[0]) ; s=int(l[1]) ; p=int(l[2])
    t=[int(x) for x in l[3::]]
    fout.write("Case #"+str(case)+": "+str(solve(s,p,t))+"\n")