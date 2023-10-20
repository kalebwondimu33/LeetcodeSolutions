class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev=releaseTimes[0]
        key=keysPressed[0]
        max_num=releaseTimes[0]
        for i in range(1,len(releaseTimes)):
            temp=releaseTimes[i]-prev
            if temp>max_num:
                max_num=temp
                key=keysPressed[i]
            elif temp==max_num:
                max_num=temp
                if key<keysPressed[i]:
                    key=keysPressed[i]
                    
            prev=releaseTimes[i]
            print(prev)
        return key