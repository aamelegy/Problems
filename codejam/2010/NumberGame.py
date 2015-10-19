def winning( A,  B):
    if (B == 0) : return True
    if (A >= 2*B) : return True
    return not winning(B, A-B) 

def solve(a1,a2,b1,b2):
    c=0
    for i in range(a1,a2+1):
        for j in range(b1,b2+1):
            if winning (i,j) or winning():
                c+=1
    return c
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    l=[int(x) for x in fin.readline().strip().split(' ')]
    a1=l[0];a2=l[1];b1=l[2];b2=l[3]
    fout.write("Case #"+str(case)+": "+str(solve(a1,a2,b1,b2))+"\n")
