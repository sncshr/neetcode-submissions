class Solution:
    def simplifyPath(self, path: str) -> str:
        data=path.split('/')
        retStck=[]
        for i in data:
            if i=='.' or i=='':
                continue
            if i=='..':
                if len(retStck)>0:
                    retStck.pop()
            else:
                retStck.append(i)
        retVal=""
        if len(retStck)==0:
            return "/"
        for i in retStck:
            retVal=retVal+'/'+i
        return retVal