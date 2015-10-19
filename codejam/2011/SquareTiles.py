    
def solve(pic,r,c):
    for i in range(r-1):
        for j in range(c-1):
            if pic[i][j]=='#' and pic[i+1][j]=='#' and pic[i][j+1]=='#' and pic[i+1][j+1]=='#':
                pic[i][j]='/'; pic[i+1][j]='\\'; pic[i][j+1]='\\'; pic[i+1][j+1]='/';
    for i in range(r):
        for j in range(c):
            if pic[i][j]=='#':
                return '\nImpossible'
    n_pic=[]
    for  r in pic:
        n_pic.append(''.join(r))
    return '\n'+'\n'.join(n_pic)   
    
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    pic=[]
    line=fin.readline().strip().split(' ')
    r=int(line[0]);c=int(line[1])
    for i in range (r):
        line=fin.readline().strip()
        pic.append(list(line))
    fout.write("Case #"+str(case)+": "+str(solve(pic,r,c))+"\n")