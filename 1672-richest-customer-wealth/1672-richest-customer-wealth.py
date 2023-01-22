class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        for i in range(len(accounts)):
            wealth=max(wealth,sum(accounts[i]))
        return wealth
            
        