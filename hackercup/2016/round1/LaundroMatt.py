from heapq import heappush, heappop
fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print case
    l,n,m,d=map(int,fin.readline().strip().split())
    w=map(int,fin.readline().strip().split())
    h = []
    dryes=[0]*min(m,1000000)
    dp=0
    done = 0
    for mac in w:
        heappush(h, (mac, mac))
    while done < l:
        x,y=heappop(h)
        done+=1
        if dryes[dp] < x:
            dryes[dp]+=x+d
        else:
            dryes[dp]+=d
        dp+=1
        dp%=m
        heappush(h, (x+y, y))
    print max(dryes)
    fout.write("Case #"+str(case)+": "+str(max(dryes))+"\n")
