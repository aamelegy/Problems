#not yet
def pre():
    jumps=dict()
    jumps[1]=1
    steps=dict()
    steps[1]=1
    for i in range(2,1000000):
        jumps[i]=jumps[i-1]+i
        steps[jumps[i-1]+i]=i
    return jumps,steps
        
    
def solve(x,y):
    pass


jumps,steps=pre()
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    x,y=int(line[0]),int(line[1])
    fout.write("Case #"+str(case)+": "+str(solve(x,y))+"\n")