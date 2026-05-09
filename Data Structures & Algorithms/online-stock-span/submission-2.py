class StockSpanner:

    def __init__(self):
        self.stck=[]
        

    def next(self, price: int) -> int:
        count=1
        if self.stck and self.stck[-1]:
            c=0
            while self.stck and self.stck[-1][0]<=price:
                c+=self.stck[-1][1]
                self.stck.pop()
            count+=c

        self.stck.append((price,count))
        return self.stck[-1][1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)