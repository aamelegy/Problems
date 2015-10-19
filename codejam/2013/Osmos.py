def solve(a,m):
    op=0
    i=-1
    while i < len(m)-1:
        i+=1
        if a > m[i]:
            a+=m[i]
        else:
            rm=len(m)-i
            diff=0
            op_t=0
            t_p=0
            while op_t<rm and diff<1 and (i+t_p)<len(m) :
                if a <= m[i+t_p]:
                    a+=a-1
                    diff-=1
                    op_t+=1
                else:
                    diff+=1
                    a+=m[i+t_p]
                    t_p+=1
            i+=max(t_p-1,0)
            op+=op_t
            if op_t==rm:
                return rm
    return op
                      
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    if case==80:
        print 'test'
    line=fin.readline().strip().split(' ')
    a,n=int(line[0]),int(line[1])
    m=fin.readline().strip().split(' ')
    for i in range(len(m)):
        m[i]=int(m[i])
    m.sort()
    fout.write("Case #"+str(case)+": "+str(solve(a,m))+"\n")