class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        ans=""
        sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        for i in sorted_dict:
            ans+=i*sorted_dict[i]
        return ans

        