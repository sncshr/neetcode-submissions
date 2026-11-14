class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            prev, val=i, arr[i]
            while 0<val<=len(arr):
                nxt=arr[val-1]
                arr[val-1]=min(0,arr[val-1])-1
                if val-1<=i or val-1==prev:
                    break
                prev=val-1
                val=nxt
        for i in range(len(arr)-1,-1,-1):
            if -arr[i]==i+1:
                return i+1
        return -1

        
        