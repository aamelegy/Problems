from sets import Set
def solve (a,b):
    set=Set()
    pairs=0
    for i in range(a,b+1):
        s_a=str(i)
        if len(s_a)==1:
            continue
        for j in range(len(s_a)-1,0,-1):
            s_p=s_a[j::]+s_a[0:j]
            if int(s_p)<=b and (s_p,s_a) not in set and s_p[0]!='0' and len(s_a)>1 and s_a !=s_p and int(s_a)<=int(s_p):
                set.add((s_p,s_a))  ; set.add((s_a,s_p)) ;pairs+=1
    return pairs
                
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    l=fin.readline().strip().split(' ')
    a=int(l[0]) ; b=int(l[1]) 
    fout.write("Case #"+str(case)+": "+str(solve(a,b))+"\n")