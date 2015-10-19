from __future__ import division
def solve (n,s):
    r=[]
    for i in range(len(s)):
        x=[0,0,0]
        wp=len(s[i][0])/(len(s[i][0])+len(s[i][1]))
        x[0]=wp
        r.append(x)
    for i in range(len(s)):
        cowp=0    
        for j in s[i][0]+s[i][1]:
            w=len(s[j][0]) ; l=len(s[j][1])
            if i in s[j][0]:
                w-=1
            if i in s[j][1]:
                l-=1
            cowp+=w/(w+l)
        cowp=cowp/len(s[i][0]+s[i][1])
        r[i][1]=cowp
    for i in range (len(s)):
        oowp=0
        coowp=0
        for j in range(len(s[i][2])):
            if s[i][2][j]=='1'or s[i][2][j]=='0':
                coowp+=1
                oowp+=r[j][1]
        r[i][2]=oowp/coowp
    x=[]
    for i in range(len(r)):
        rpi=0.25*r[i][0]+0.5*r[i][1]+0.25*r[i][2]
        x.append(str(rpi))
    return '\n'+'\n'.join(x)
        
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    n=int(fin.readline().strip())
    s=[]
    for i in range(n):
        temp=fin.readline().strip()
        x=([],[],temp)
        for j in range(len(temp)):
            if temp[j]=='1':
                x[0].append(j)
            elif temp[j]=='0':
                x[1].append(j)
        s.append(x)
    fout.write("Case #"+str(case)+": "+str(solve(n,s))+"\n")