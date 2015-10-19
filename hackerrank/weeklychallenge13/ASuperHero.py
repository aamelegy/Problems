def read_integers():
    return [int(x) for x in raw_input().strip().split()]
t=input()
for _ in range(t):
    n,m=read_integers()
    p,b,ad=[],[],[]
    for i in range(n):
        p.append(read_integers())
    b.append([0]*m)
    for i in range(n-1):
        b.append(read_integers())
    read_integers()
    ad.append([0]*m)
    for i in range(n):
        ad.append([99999999999]*m)
    for i in range(n):
        for j in range(m):
            for k in range(m):
                ad[i+1][j]=min(max(0,p[i][j]-b[i][k])+ad[i][k],ad[i+1][j])
    print min(ad[i+1])
        
    
        
            