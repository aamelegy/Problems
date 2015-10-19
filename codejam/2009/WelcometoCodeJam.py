def solve(s):
    st=[0]*len(msg)
    for ch in s:
        for i in range(len(st)):
            if msg[i]==ch:
                if i==0:
                    st[i]+=1
                else:
                    st[i]+=st[i-1]
    temp=str(st[len(st)-1]).zfill(4)
    return temp[len(temp)-4::]
msg='welcome to code jam'
fin=open('in','r') ; fout=open('out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    s=fin.readline().strip()
    fout.write("Case #"+str(case)+": "+str(solve(s))+"\n")