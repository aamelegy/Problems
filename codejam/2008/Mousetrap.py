#small
def incp(p,i,l):
    p=(i+p)%l
    return p
def solve(k,ind):
    deck=[(x,'-1') for x in range(k)]
    sol=['-1' for x in range(k)]
    c=1 ; p=0
    for i in range(1,k+1):
        print i
        while True:
            if i==c:
                sol[deck[p][0]]=str(i) ; c=1 ; del deck[p]
                if p==len(deck):
                    p=0
                break
            diff=i-c
            p=incp(p,diff,len(deck)) ;c+=diff
    return ' '.join([sol[x-1] for x in ind])
            
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    k=int(fin.readline().strip())
    ind=[int(x) for x in fin.readline().strip().split(' ')]
    ind=ind[1::]
    fout.write("Case #"+str(case)+": "+str(solve(k,ind))+"\n")