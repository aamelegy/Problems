
def calc(x):
    return (x*(x+1))/2

fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print case
    n,p=map(int,fin.readline().strip().split())
    a=map(int,fin.readline().strip().split())
    p1,p2,sm=0,0,0
    sm=a[p1]
    last=[-1,-1]
    current=[-1,-1]
    r=[]
    re=0
    while p2<n:
        if sm<=p:
            current=[p1,p2]
            p2+=1
            if p2 == n:
                break
            sm+=a[p2]
        else:
            if current != [-1,-1]:
                re+=calc(current[1]-current[0]+1)
                if last[1] >= current[0]:
                    re-=calc(last[1]-current[0]+1)
            last=current
            sm-=a[p1]
            p1+=1
            if p1>p2:
                p2+=1
                if p2 == n:
                    break
                sm+=a[p2]
    if current != [-1,-1]:
        re+=calc(current[1]-current[0]+1)
        if last[1] >= current[0]:
            re-=calc(last[1]-current[0]+1)
    print re
    fout.write("Case #"+str(case)+": "+str(re)+"\n")










