class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            flag = 1
            for char in word:
                if chars.count(char) < word.count(char):
                    flag = 0
                    break
            if flag:
                ans += len(word)
        return ans
        