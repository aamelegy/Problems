def solve(n,k):
    temp=(2**n)-1
    t=k-temp
    if k==temp or t %(temp+1)==0:
        return "ON"
    else:
        return "OFF"
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    n=int(line[0]) ; k= int(line[1])
    fout.write("Case #"+str(case)+": "+str(solve(n,k))+"\n")