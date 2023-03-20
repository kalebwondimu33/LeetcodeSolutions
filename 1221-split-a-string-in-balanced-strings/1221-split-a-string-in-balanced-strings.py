class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left=0
        count=0
        for right in range(2,len(s)+1,2):
            temp=s[left:right]
            if temp.count("R")==temp.count("L"):
                count+=1
                left=right
        return count
        