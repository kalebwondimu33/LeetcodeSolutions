class Solution:
    def secondHighest(self, s: str) -> int:
        result=set()
        if s.isalpha():
            return -1
        for i in s:
            if i.isnumeric():
                result.add(int(i))
        if len(result)==1:
            return -1
        else:
            result.remove(max(result))
            return max(result)
        