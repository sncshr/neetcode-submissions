class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        retCount=0
        if n==0:
            return True
        if len(flowerbed)==1:
            if n==1:
                return flowerbed[0]==0
        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i+1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    retCount+=1
                    continue
            if i>=len(flowerbed)-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0:
                    retCount+=1
                    flowerbed[i]=1
                continue
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                retCount+=1
                flowerbed[i]=1
        return retCount>=n
        