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
        return ('/' + '/'.join(retStck))