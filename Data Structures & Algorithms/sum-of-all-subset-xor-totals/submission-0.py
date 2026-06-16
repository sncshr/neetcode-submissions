class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret=0
        for i in nums:
            ret=ret | i
        return ret * (2**(len(nums)-1))

        