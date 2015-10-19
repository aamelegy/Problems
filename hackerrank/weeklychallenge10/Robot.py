import random

n=input()
v,p=[],[]
for i in range(n):
    line=[int(x) for x in raw_input().strip().split(" ")]
    v.append(line[0])
    p.append(line[1])
score = 0
def Go(step, energy):
    global score
    if step == n:
        score += v[step]
        return (score);
    else: 
        way=random.randint(1, 2)
        if (way == 1):
            score += v[step]
        else:
            energy = p[step]
        if (energy > 0):
            Go(step + 1, energy - 1);
        else:
            print ""
while True:
    print Go(1,0)