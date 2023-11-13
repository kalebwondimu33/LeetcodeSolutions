class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans, stack = 0, []
        for c in s: 
            if c == "(": 
                stack.append(ans)
                ans = 0
            else: ans = max(1, 2*ans) + stack.pop()
        return ans
            
        