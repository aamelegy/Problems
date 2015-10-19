

def nextjob(i,v):
    for j in range (i+1,len(v)):
        if v[j]>v[i]:
            return j
    return -1
    
def solve(e,r,v):
    mx_e=e
    gain=0
    for i in range(len(v)):
        n=nextjob(i,v)
        if n!=-1:
            joule=min(((n-i)*r+e)-(mx_e),mx_e)
            if joule >0:
                e-=joule
                gain+=joule*v[i]
            e+=r
        else:
            gain+=e*v[i]
            e=r
    return gain    
            
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    e,r,n=int(line[0]),int(line[1]),int(line[1])
    v=fin.readline().strip().split(' ')
    for i in range(len(v)):
        v[i]=int(v[i])
    fout.write("Case #"+str(case)+": "+str(solve(e,r,v))+"\n")