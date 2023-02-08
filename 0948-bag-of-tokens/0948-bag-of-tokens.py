class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        points = 0
        max_points = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                points += 1
                max_points = max(max_points, points)
            elif points > 0:
                power += tokens[right]
                right -= 1
                points -= 1
            else:
                break
        return max_points




        