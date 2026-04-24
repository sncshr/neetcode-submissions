class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm={0:1}
        retCount=0
        left=0
        for i in nums:
            left+=i
            retCount+=hm.get(left-k,0)
            hm[left]=1+hm.get(left,0)
        return retCount


