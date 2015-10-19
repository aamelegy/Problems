a=[1]*1000000
for i in range(2,1000000):
    for j in range(1,1000000/i):
        a[j*i-1]+=i*i*i*i
        