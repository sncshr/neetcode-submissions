class MyHashSet:

    def __init__(self):
        self.bucketSize=10000
        self.arr=[False]*self.bucketSize

    def add(self, key: int) -> None:
        self.arr[key%self.bucketSize]=True

    def remove(self, key: int) -> None:
        self.arr[key%self.bucketSize]=False
        

    def contains(self, key: int) -> bool:
        return self.arr[key%self.bucketSize]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)