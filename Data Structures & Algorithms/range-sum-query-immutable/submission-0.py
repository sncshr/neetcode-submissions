class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix=[]
        c=0
        for i in nums:
            c+=i
            self.prefix.append(c)
        

    def sumRange(self, left: int, right: int) -> int:
        r=self.prefix[right]
        l=0
        if left>0:
            l=self.prefix[left-1]
        return r-l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)