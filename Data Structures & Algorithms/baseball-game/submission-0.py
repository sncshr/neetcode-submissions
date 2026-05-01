class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck=[]
        ops=["+","C","D"]
        for i in operations:
            if i not in ops:
                stck.append(int(i))
            else:
                if i=="+":
                    stck.append(stck[-1]+stck[-2])
                elif i=="D":
                    stck.append(2*stck[-1])
                else:
                    stck.pop()
        return sum(stck)
        