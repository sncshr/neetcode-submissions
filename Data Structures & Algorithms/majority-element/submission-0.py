class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=0
        maxVotes=0
        for i in range(len(nums)):
            if maxVotes==0:
                candidate=nums[i]
                maxVotes+=1
            elif candidate==nums[i]:
                maxVotes+=1
            else:
                maxVotes-=1
        return candidate
            
        