__author__ = 'sshadmin'

n,m = map(int,raw_input().strip().split())
a = map(int,raw_input().strip().split())
b = map(int,raw_input().strip().split())

a.sort()
b.sort()
pa=pb=0

c=0
while pa<len(a) and pb<len(b):
    if b[pb] >= a[pa]:
        c += 1
        pb += 1
        pa += 1
    else:
        pb += 1
print len(a)-c