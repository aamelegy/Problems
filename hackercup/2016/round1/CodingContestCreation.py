fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print case
    n=int(fin.readline())
    d=map(int,fin.readline().strip().split())
    r=[]
    sm=0
    i=0
    while i < len(d):
        st = list(d[i:i+4])
        c=[st[0]]
        j=0
        while j < len(st)-1:
            dff=st[j+1] - st[j]
            if j ==0:
                if dff >0 and dff <= 10:
                    j+=1
                elif dff > 0 and dff <=20:
                    i-=1
                    sm+=1
                    j+=1
                elif dff > 0 and dff <=30:
                    i-=2
                    sm+=2
                    j+=3
                    break
                else:
                    i-=3
                    sm+=3
                    j+=3
                    break
            elif j==1:
                if dff >0 and dff <= 10:
                    j+=1
                elif dff > 0 and dff <=20:
                    i-=1
                    sm+=1
                    j+=2
                else:
                    i-=2
                    sm+=2
                    j+=2
            elif j ==2:
                if dff >0 and dff <= 10:
                    j+=1
                else:
                    i-=1
                    sm+=1
                    j+=1
        for _ in range(3-j):
            sm+=1
        c=[]
        i+=4
    print sm
    fout.write("Case #"+str(case)+": "+str(sm)+"\n")




