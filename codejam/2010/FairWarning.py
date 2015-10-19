def GCD(a,b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b
def solve(L):
    y = L[0]
    L1 = [abs(x - y) for x in L]
    g=reduce(GCD,L1)
    if y % g == 0:
        return 0
    else:
        return g - (y % g)
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    l=[int(x) for x in fin.readline().strip().split(' ')][1::]
    fout.write("Case #"+str(case)+": "+str(solve(l))+"\n")