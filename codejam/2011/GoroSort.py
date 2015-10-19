def solve (n):
    s=sorted(n)
    sw=0
    for i in range(len(s)):
        if n[i]!=s[i]:
            sw+=1
    return float(sw)
        
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    fin.readline()
    n=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(n))+"\n")