class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hm=set()
        for i in emails:
            local, domain=i.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            hm.add((local,domain))
        return len(hm)


        