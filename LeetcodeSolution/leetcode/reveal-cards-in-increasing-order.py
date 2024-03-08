class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result= deque()
        deck.sort(reverse = True)

        for num in deck:
            if result:
                result.appendleft(result.pop())
            
            result.appendleft(num)

        return result
        