class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        hashtable={"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6","h":"7","i":"8","j":"9"}
        count1=""
        count2=""
        target=""
        for i in firstWord:
            count1+=hashtable[i]
        for j in secondWord:
            count2+=hashtable[j]
        for i in targetWord:
            target+=hashtable[i]
        if int(count1)+int(count2)==int(target):
            return True
        else:
            return False
            