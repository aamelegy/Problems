def calcexpd(l,limit):
    w=[]
    for i in range(len(l)):
        if l[i] <= limit:
            limit-=l[i]
            w.append(l[i])
        else:
            break
    if limit != 0:
        w.append(limit)
    sm=sum(w)
    w=map(lambda x: (x/2.0) * (x*1.0/sm),w)
    return sum(w)

def calcexpdre(l,limit):
    w=[]
    for i in range(len(l)-1,-1,-1):
        if l[i] <= limit:
            limit-=l[i]
            w.append(l[i])
        else:
            break
    if limit != 0:
        w.append(limit)
        sm=sum(w)
        w1=map(lambda x: (x/2.0) * (x*1.0/sm),w[0:len(w)-1])
        w1.append((2*l[i]-limit) /2.0 * (limit*1.0/sm))
    else:
        sm=sum(w)
        w1=map(lambda x: (x/2.0) * (x*1.0/sm),w[0:len(w)-1])
    return sum(w1)

fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print case
    n,a,b=map(int,fin.readline().strip().split())
    c=map(int,fin.readline().strip().split())
    sm=sum(c)
    be=a%sm
    if be!=0:
        be = sm-be
    af=b%sm
    na=a+be
    nb=b-af
    total = calcexpd(c,sm) * ((nb-na)*1.0 / (b-a) ) + calcexpdre(c,be) *(be*1.0 / (b-a) )+ calcexpd(c,af) *(af*1.0 / (b-a) )
    fout.write("Case #"+str(case)+": "+str(total)+"\n")