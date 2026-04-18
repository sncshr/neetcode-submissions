class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hm={}
        for i in hand:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        minHeap=list(hm.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first=minHeap[0]
            for i in range(first,first+groupSize):
                if i not in hm:
                    return False
                hm[i]-=1
                if hm[i]==0:
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
            
        return True