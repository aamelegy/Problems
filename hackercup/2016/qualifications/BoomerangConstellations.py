fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print case
    n = int(fin.readline())
    p=[]
    for _ in range(n):
        p.append(map(int,fin.readline().strip().split()))
    d=dict()
    for i in range(n):
        for j in range(n):
            if i ==j:
                continue
            p1=p[i]
            p2=p[j]
            distance = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
            pair = (i, distance)
            if pair not in d:
                d[pair]=0
            d[pair]+=1
    sm=0
    for key in d:
        sm+=((d[key]-1)*(d[key]))/2
    fout.write("Case #"+str(case)+": "+str(sm)+"\n")




