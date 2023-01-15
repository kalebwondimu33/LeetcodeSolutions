class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_ip=""
        for i in address:
            if i==".":
                defanged_ip+="[.]"
            else:
                defanged_ip+=i
        return defanged_ip
        