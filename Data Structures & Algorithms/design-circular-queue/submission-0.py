
class Node:
    def __init__(self, val, prevNode,nextNode):
        self.val=val
        self.prevNode=prevNode
        self.nextNode=nextNode
class MyCircularQueue:

    def __init__(self, k: int):
        self.left=Node(-1,None,None)
        self.right=Node(-1,self.left,None)
        self.left.nextNode=self.right
        self.k=k
        self.currLen=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = Node(value,self.right.prevNode,self.right)
        self.right.prevNode.nextNode=curr
        self.right.prevNode=curr
        self.currLen+=1
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        toRemove=self.left.nextNode
        self.left.nextNode=toRemove.nextNode
        toRemove.nextNode.prevNode=self.left
        self.currLen-=1
        return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nextNode.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prevNode.val
        

    def isEmpty(self) -> bool:
        return self.currLen==0
        

    def isFull(self) -> bool:
        return self.currLen==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()