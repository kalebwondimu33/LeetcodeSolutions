class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_Time=60*int(current[:2])+int(current[3:])
        target_Time=60*int(correct[:2])+int(correct[3:])
        diff=target_Time-current_Time
        count=0
        for i in [60,15,5,1]:
            count+=diff//i
            diff%=i
        return count
            
            