def read_integers():
    return [int(x) for x in raw_input().strip().split()]
n,q=read_integers()
a=read_integers()
com=[0]*(n+1)
minl,maxr=1,n
dirty=1
for _ in range(q):
    t,l,r=read_integers()
    if t==2:
        if dirty==1:
            for i in range(minl,maxr+1):
                com[i]=com[i-1]+a[i-1]
            dirty=0
            minl,maxr=n,0
        print com[r]-com[l-1]
    elif t==1:
        for i in range(l-1,r,2):
            a[i],a[i+1]=a[i+1],a[i]
        dirty=1
        minl=min(minl,l)
        maxr=max(maxr,r)        
            
    