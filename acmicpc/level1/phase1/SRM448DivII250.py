class TheBlackJackDivTwo():
    def score(self, cards):
        c_d={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'K':10,'J':10,'Q':10,'A':11}
        return sum([c_d[x[0]] for x in cards])
