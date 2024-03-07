class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashtable = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans=[]
        def backtrack(start,path=[]):
            if not digits:
                return []
            if len(path) == len(digits):  # Check if path length equals digits length
                ans.append("".join(path))  # Append the formed string to ans
                return

            temp = hashtable[digits[start]]
            for j in range(len(temp)):
                path.append(temp[j])
                backtrack(start + 1, path)  # Increment start instead of i
                path.pop()

        backtrack(0)
        return ans