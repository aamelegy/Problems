


class CheckFunction():
    def newFunction(self, code):
        sum=0
        dashes=[6,2,5,5,4,5,6,3,7,6]
        for ch in code:
            sum+=dashes[int(ch)]
        return sum
    