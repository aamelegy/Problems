
class BootsExchange():
    def leastAmount(self, left, right):
        left=list(left) 
        for boot in right:
            if boot in left:
                left.remove(boot)
        return len(left)