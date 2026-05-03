class MyQueue:

    def __init__(self):
        self.stckA=[]
        self.stckB=[]

    def push(self, x: int) -> None:
        self.stckA.append(x)
    def pop(self) -> int:
        if not self.stckB:
            while self.stckA:
                self.stckB.append(self.stckA.pop())
        return self.stckB.pop()   
    def peek(self) -> int:
        if not self.stckB:
            while self.stckA:
                self.stckB.append(self.stckA.pop())
        return self.stckB[-1]       

    def empty(self) -> bool:
        return max(len(self.stckA),len(self.stckB))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()