def solve(l):
    stack=[]
    for w in l:
        stack.append(w)
    rev=[]
    while (len(stack)>0):
        rev.append(stack.pop())
    return ' '.join(rev)
        
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    l=fin.readline().strip().split(' ')
    fout.write("Case #"+str(case)+": "+str(solve(l))+"\n")