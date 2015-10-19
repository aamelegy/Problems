def solve (r,t):
    hi=t ; lo=1
    while lo<=hi:
        mi=(hi+lo)/2
        tf=(2*r+2*mi-1)*mi
        if tf >t:
            hi=mi-1 
        else :
            lo=mi+1 ; res=mi
    return res     
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    r,t=int(line[0]),int(line[1])
    fout.write("Case #"+str(case)+": "+str(solve(r,t))+"\n")