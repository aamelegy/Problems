def follows(patt , wo):
    for i in range(len(pat)):
            if wo[i] not in pat[i]:
                return False
    return True
def solve(pat,w):
    c=0
    for wo in w:
        if follows(pat , wo):
            c+=1
    return c

fin=open('../in','r') ; fout=open('../out','w')
line=fin.readline().strip().split(' ')
l=int(line[0]) ; d=int(line[1]); cases=int(line[2])
w=[]
for word in range(d):
    w.append(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip()
    st=[]
    pat=[]
    c_l=[]
    for ch in line:
        if ch=='(':
            st.append(ch)
            continue
        elif ch==')':
            st.pop()
            pat.append(c_l)
            c_l=[]
            continue
        if len(st)>0:
            c_l.append(ch)
        else:
            pat.append([ch])
    fout.write("Case #"+str(case)+": "+str(solve(pat,w))+"\n")