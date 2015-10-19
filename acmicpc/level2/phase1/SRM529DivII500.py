import operator

class KingSort():
    def getSortedList(self, kings):
        kings=list(kings)
        tens=["XXX","XL","XX","L","X"]
        tensv=[30,40,20,50,10]
        ones=["VIII","VII","III","IX","II","IV","VI","I","V"]
        onesv=[8,7,3,9,2,4,6,1,5]
        for i in range(len(kings)):
            tmp=kings[i]
            kings[i]=kings[i].split(' ')
            kings[i].append(tmp)
            ten=0
            sm=0
            for j in range(len(tens)):
                if kings[i][1][0:len(tens[j])]==tens[j]:
                    sm+=tensv[j]
                    ten=len(tens[j])
                    break
            for j in range(len(ones)):
                if kings[i][1][ten::]==ones[j]:
                    sm+=onesv[j]
                    break
            kings[i][1]=sm
        kings.sort(key=operator.itemgetter(0,1))
        return [x[2] for x in kings]
            
        