class solution():
    def find_max(self,prices):
        curmax=0
        finalmax = 0
        for i in range(1, len(prices)):
            curmax += prices[i] - prices[i-1]
            curmax = max(0, curmax)
            finalmax = max(curmax, finalmax)
            
        return finalmax
    
if __name__ == '__main__':
    a = solution()
    print(a.find_max([7,1,5,3,6,4]))
        
