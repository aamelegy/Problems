

def solve(a,b,ta):
    t_a=[0]*1500 ;t_b=[0]*1500
    for e in a:
        t_a[e[0]]-=1 ;t_b[e[1]+ta]+=1
    for e in b:
        t_b[e[0]]-=1 ;t_a[e[1]+ta]+=1
    c=0 ;ta=0 ;tb=0
    for s in t_a:
        c+=s
        if c<0:
            ta+=-1*c ;c=0
    c=0
    for s in t_b:
        c+=s
        if c<0:
            tb+=-1*c ;c=0
    return str(ta)+" "+str(tb)

fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    ta=int(fin.readline().strip())
    line=fin.readline().strip().split(' ')
    na,nb=int(line[0]),int(line[1])
    a=[] ; b=[]
    for i in range(na):
        line=fin.readline().strip().split(' ')
        x=int(line[0][:-3]) * 60 + int(line[0][-2:])
        y=int(line[1][:-3]) * 60 + int(line[1][-2:])
        a.append((x,y))
    for i in range(nb):
        line=fin.readline().strip().split(' ')
        x=int(line[0][:-3]) * 60 + int(line[0][-2:])
        y=int(line[1][:-3]) * 60 + int(line[1][-2:])
        b.append((x,y))
    fout.write("Case #"+str(case)+": "+str(solve(a,b,ta))+"\n")