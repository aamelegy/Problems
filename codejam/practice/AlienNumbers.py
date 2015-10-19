num_rep=dict()
for i in range (0,99):
    num_rep[i]=chr(i)
def base10toN(num,n,tl):
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        remainder_string=num_rep[remainder]
        new_num_string=remainder_string+new_num_string
        current=current/n
    return new_num_string

def solve(nu,sl,tl):
    bases=len(sl) ; baset=len(tl)
    nl=list(nu)
    decimal=0
    j=0
    for i in range(len(nl)-1,-1,-1):
        decimal+=sl.index(nl[i])*(bases**j)
        j+=1
    target=base10toN(decimal,baset,tl)
    tm=list(str(target))
    for i in range(len(tm)):
        tm[i]=tl[ord(tm[i])]
    return ''.join(tm)
    
        
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    line=fin.readline().strip().split(' ')
    nu=line[0];sl=line[1];tl=line[2]
    fout.write("Case #"+str(case)+": "+str(solve(nu,sl,tl))+"\n")