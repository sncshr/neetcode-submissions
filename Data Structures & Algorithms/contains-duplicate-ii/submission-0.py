class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm=defaultdict(set)
        count=0
        for idx,v in enumerate(nums):
            hm[v].add(idx)
        for idx,v in enumerate(nums):
            if v in hm:
                for i in hm[v]:
                    if i!=idx and abs(idx-i)<=k:
                        count+=1
                    if count==2:
                        return True
        return False


        