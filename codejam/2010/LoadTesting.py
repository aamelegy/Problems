def solve(l,p,c):
    count=0
    while(l* c**(2**count) < p):
        count += 1
    return count
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(line[0],line[1],line[2]))+"\n")