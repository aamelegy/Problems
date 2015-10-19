

class AccountBalance():
    def processTransactions(self, startingBalance, transactions):
        for t in transactions:
            t=t.split(' ')
            if t[0]=="D":
                startingBalance-=int(t[1])
            else:
                startingBalance+=int(t[1])
        return startingBalance
                
                
    
