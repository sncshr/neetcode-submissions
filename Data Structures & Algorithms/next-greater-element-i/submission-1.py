class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        for i in range(len(nums1)):
            hm[nums1[i]]=i
        ret = [-1]*len(nums1)
        stck=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stck and curr>stck[-1]:
                v=stck.pop()
                idx=hm[v]
                ret[idx]=curr
            if curr in hm:
                stck.append(curr)
        return ret


        
        

        