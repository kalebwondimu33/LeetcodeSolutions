class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and item[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and item[2] == ruleValue:
                count += 1
        return count
                    
        