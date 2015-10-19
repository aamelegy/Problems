def is_con(s):
    vowels={'a', 'e', 'i', 'o','u'}
    for char in s:
        if char in vowels:
            return False
    return True
def solve(s,n):
    cons=[]
    res=0
    for i in range(len(s)):
        if i+n <=len(s):
            temp=s[i:i+n]
            if is_con(temp):
                cons.append((i,i+n-1))
    for i in range(len(cons)):
        res+=(cons[i][0]+1)*(len(s)-cons[i][1])
        res-=(i)*(len(s)-cons[i][1])
    return res
            
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    s,n=line[0],int(line[1])
    fout.write("Case #"+str(case)+": "+str(solve(s,n))+"\n")