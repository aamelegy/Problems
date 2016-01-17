fout=open("out","w")
fin =open("in")
t=int(fin.readline())
for case in range(1,t+1):
    print case
    n=int(fin.readline())
    r1=["X"]+list(fin.readline().strip())+["X","X"]
    r2=["X"]+list(fin.readline().strip())+["X"]
    added=False
    sm=0
    for i in range(1,n+1):
        if r1[i]==".":
            if r2[i-1] == "X" and r2[i+1] == "X" and not added:
                r1[i]="G"
                sm+=1
                added = True
            elif i == n and not added:
                r1[i]="G"
                sm+=1
                added = True
        elif r1[i] == "X":
            if i !=1 and not added and r1[i-1]==".":
                r1[i-1]="G"
                sm+=1
            else:
                added = False
    added = False
    i=0
    c=0
    first = False
    for i in range(1,n+2):
        if r1[i-1] == "X" and r1[i+1] =="X" and r1[i]=="G" :
            first = True

        if r2[i] != "X":
            c+=1
        elif i !=1:
            if c>1 and not first:
                sm+=1
            elif c==1 and r1[i-1] != "G":
                sm+=1
            first =False
            c=0
    print r1
    print r2
    print sm
    fout.write("Case #"+str(case)+": "+str(sm)+"\n")








