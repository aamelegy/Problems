from collections import namedtuple
like=namedtuple('like','milk malted')
def solve(cs,n):
    flv=['0']*n
    solved=False
    nosol=False
    while(not solved):
        print 'another loop'
        if nosol:
            return 'IMPOSSIBLE'
        for i in  range(len(cs)):
            exceptmalted=True ;maltindex=0
            for j in range(len(cs[i].milk)):
                if cs[i].malted[j]=='0' and flv[cs[i].milk[j]-1]=='0':
                    exceptmalted=False
                elif cs[i].malted[j]=='1' and flv[cs[i].milk[j]-1]=='1':
                    exceptmalted=False ; 
                elif cs[i].malted[j]=='1':
                    maltindex=j
            if exceptmalted:
                flv[cs[i].milk[maltindex]-1]='1'          
        solved=True
        for i in  range(len(cs)):
            cusat=False
            for j in range (len(cs[i].milk)):
                if flv[cs[i].milk[j]-1] ==cs[i].malted[j]:
                    cusat=True
            if not cusat :
                solved =False
                if '1' not in cs[i].malted:
                    nosol=True
                break
        print ' '.join(flv)
    return ' '.join(flv)
         
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    n=int(fin.readline().strip())
    c=int(fin.readline().strip())
    cs=[]
    for i in range(c):
        temp=[] ;milk=[];malted=[]
        line=fin.readline().strip().split(' ')
        for j in range(1,len(line),2):
            milk.append(int(line[j]));malted.append(line[j+1])
        cs.append(like(milk,malted))
    fout.write("Case #"+str(case)+": "+str(solve(cs,n))+"\n")