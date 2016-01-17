m=[2,4,7]


for j in range(1,50):
    mul=[]
    for num in m:
        for i in range(1,j+1):
            mul.append([num*i,num])
    mul.sort(key=lambda x:x[0])

    print j,mul[j-1],mul[0:j]