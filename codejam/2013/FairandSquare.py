import itertools
def ispal(s):
    st=str(int(s))
    if st[len(st):len(st)-1-len(st)/2:-1]==st[0:len(st)/2]:
        return True
    else:
        return False
def solve(s,e):
    c=0
    for i in range(s,e+1):
        if i in fair:
            c+=1
    return c

def pre():
    fair=set()
    for i in range(10**7):
        print i
        if ispal(i):
            if ispal(i*i):
                fair.add(i*i)
    return fair

fair=pre()    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip().split(' ')
    s=int(line[0]); e=int(line[1])
    fout.write("Case #"+str(case)+": "+str(solve(s,e))+"\n")