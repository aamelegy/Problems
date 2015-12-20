__author__ = 'a-ahelme'

d,sumtime=map(int,raw_input().strip().split())
t,r=[],[]
for i in range(d):
    mn,mx=map(int,raw_input().strip().split())
    t.append([mn,mx])
for i in range(len(t)):
    r.append(t[i][0])
    sumtime-=t[i][0]
if sumtime <0:
    print "NO"
elif sumtime>0:
    for i in range(len(t)):
        r[i]+=min(t[i][1]-t[i][0],sumtime)
        sumtime-=min(t[i][1]-t[i][0],sumtime)
        if sumtime == 0:
            break
    if sumtime>0:
        print "NO"
    else:
        print "YES"
        print " ".join(map(str,r))
elif sumtime ==0:
    print "YES"
    print " ".join(map(str,r))




