class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hashtable={"U":0,"D":0,"R":0,"L":0}
        for i in moves:
            hashtable[i]+=1
        if hashtable["U"]==hashtable["D"] and hashtable["L"]==hashtable["R"]:
            return True
        else:
            return False
        
        