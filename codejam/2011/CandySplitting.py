xor=lambda x,y :x^y
def solve (c):
    c.sort()
    for i in range(1,len(c)):
        pile1=reduce(xor,c[0:i])
        pile2=reduce(xor,c[i::])
        if pile1==pile2:
            return sum(c[i::])
    return "NO"
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    fin.readline()
    c=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(c))+"\n")