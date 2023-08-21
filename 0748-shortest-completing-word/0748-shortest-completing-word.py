class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = Counter(ltr.lower() for ltr in licensePlate if ltr.isalpha())
        return min((word for word in words if not letters - Counter(word)), key=len)
        