def solve(w,b):
    if int(b)%2==0:
        return 'WHITE'
    else:
        return 'BLACK'
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    b=line[1];w=line[0]
    fout.write("Case #"+str(case)+": "+str(solve(w,b))+"\n")