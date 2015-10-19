def solve(n,m,a):
    if a>n*m:
        return 'IMPOSSIBLE'
    for i in range(1,n+1):
        if a%i==0:
            j=a/i
        else:
            j=a/i+1
        if j>=m+1:
            continue
        for k in range(1,i+1):
                l=(i*j-a)/k
                if l >= 0 and a == i*j - k*l:
                    return '0 0 %d %d %d %d' % (k, j, i, l)
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip().split(' ')
    n=int(line[0]) ;m=int(line[1]);a=int(line[2])
    fout.write("Case #"+str(case)+": "+str(solve(n,m,a))+"\n")