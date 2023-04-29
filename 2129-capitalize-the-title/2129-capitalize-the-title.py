class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=title.split()
        for i,v in enumerate(words):
            if len(v)<=2:
                words[i]=v.lower()
            else:
                words[i]=v.title()
        return " ".join(words)
        