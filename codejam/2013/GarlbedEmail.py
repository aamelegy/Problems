#incorrect
from collections import namedtuple
State=namedtuple('state','prefix end last changes')
indices=[[],[1],[1,2],[1,3]]
def solve(line):
    q=[] ;states=dict() ;q.append(State('',-1,-10,0)) ; sol=[]
    while len(q)>0:
        state=q.pop()
        print state.prefix
        if len(state.prefix)==len(line):sol.append(state.changes);continue
        for i in range(1,11):
            st=line[state.end+1:1+state.end+i]
            for index in indices:
                for k in range(max(-state.end+state.last+5-1,0),len(st)):
                    temp=list(st)
                    if len(index)==0 or k+(index[len(index)-1]-1)*5<len(temp):
                        if len(index)==0:last_change=0
                        else:last_change=k+(index[len(index)-1]-1)*5
                        for ind in index:
                            temp[k+(ind-1)*5]='*'
                        if ''.join(temp) in dic and (len(temp)+len(state.prefix) not in states or states[len(temp)+len(state.prefix)]>state.changes+len(index)):
                            sta=State(state.prefix+''.join(temp),state.end+len(temp),last_change+state.end+1,state.changes+len(index))
                            q.append(sta)
                            states[len(temp)+len(state.prefix)]=state.changes+len(index)
    sol.sort() 
    if len(sol)==0:
        return -1 
    print sol[0]
    return sol[0]
def pre():
    dic=set()
    fdic=open('dic.txt','r')
    line=fdic.readline().strip()
    c=0
    while line!='':
        c+=1
        print c
        for index in indices:
            for j in range(len(line)):
                temp=list(line)
                if len(index)==0 or j+(index[len(index)-1]-1)*5<len(temp):
                    for ind in index:
                        t=j+(ind-1)*5
                        if t <len(temp):
                            temp[t]='*'
                    dic.add(''.join(temp))
        line=fdic.readline().strip()
    return dic
dic=pre()
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip()
    fout.write("Case #"+str(case)+": "+str(solve(line))+"\n")