class Solution:
    def decodeString(self, s: str) -> str:
        finalStr=''
        stck=[]
        for i in range(len(s)):
            if s[i]!=']':
                stck.append(s[i])
            else:
                sub=''
                while stck and stck[-1]!='[':
                    sub=stck.pop()+sub
                stck.pop()
                k=''
                while stck and stck[-1].isdigit():
                    k=stck.pop()+k
                stck.append(int(k)*sub)
        return "".join(stck)
        