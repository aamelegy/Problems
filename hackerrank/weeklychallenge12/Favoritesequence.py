import operator
n=input()
d=dict()
for _ in range(n):
    tmp=[int(x) for x in raw_input().strip().split()]
    tmp=tmp[1::]
    for i in range(len(tmp)-1,-1,-1):
        if tmp[i] not in d:
            d[tmp[i]]=set()
        d[tmp[i]]|=set(tmp[0:i])
data=[]
for key in d:
    data.append([key,d[key]])
data.sort(key=operator.itemgetter(0))
found=set()
r=[]
for _ in range(len(data)):
    for i in range(len(data)): 
        if data[i][0] not in found:
            if data[i][1]-found==set([]):
                found.add(data[i][0])
                r.append(data[i][0])
                break
print " ".join(map(str,r))