class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        retCount=0
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    retCount += 1

                    if retCount >= n:
                        return True

            # if i==0:
            #     if flowerbed[i+1]==0 and flowerbed[i]==0:
            #         flowerbed[i]=1
            #         retCount+=1
            #         continue
            # if i>=len(flowerbed)-1:
            #     if flowerbed[i-1]==0 and flowerbed[i]==0:
            #         retCount+=1
            #         flowerbed[i]=1
            #     continue
            # if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
            #     retCount+=1
            #     flowerbed[i]=1
        return retCount>=n
        