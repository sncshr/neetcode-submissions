class MinStack:

    def __init__(self):
        self.minVal=[]
        self.stck=[]
    def push(self, val: int) -> None:
        self.stck.append(val)
        minVal=min(val, self.minVal[-1] if self.minVal else val)
        self.minVal.append(minVal)

    def pop(self) -> None:
        self.minVal.pop()
        self.stck.pop()
        

    def top(self) -> int:
        return self.stck[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        
