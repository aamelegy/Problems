
from collections import Counter

class DistanceBetweenStrings():
    def getDistance(self, a, b, letterSet):
        su =0
        a=a.lower()
        b=b.lower()
        counter_a=Counter(a)
        counter_b=Counter(b)
        letterSet=letterSet.lower()
        for ch in letterSet:
            n1=counter_a[ch]
            n2=counter_b[ch]
            su+=(n1-n2)**2
        return su