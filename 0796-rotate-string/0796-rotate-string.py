class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ss=len(s)
        go=len(goal)
        if ss!=go:
            return False
        temp=s+s
        return temp.find(goal)!=-1