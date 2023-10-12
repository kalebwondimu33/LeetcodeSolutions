class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count_s=Counter(s)
        return min(count_s[i]//count for i,count in Counter(target).items())