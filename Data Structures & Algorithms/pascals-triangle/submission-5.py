class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        retArr=[[1]]
        for i in range(numRows-1):
            temp=[0]+retArr[-1]+[0]
            row=[]
            for j in range(len(retArr[-1])+1):
                row.append(temp[j]+temp[j+1])
            retArr.append(row)
        return retArr

        