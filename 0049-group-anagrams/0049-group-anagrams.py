class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_arr=list(map(lambda s:''.join(sorted(s)),strs))
        hashtable={}
        for i in range(len(sorted_arr)):
            if sorted_arr[i] in hashtable:
                hashtable[sorted_arr[i]].append(strs[i])
            else:
                hashtable[sorted_arr[i]]=[strs[i]]
        return hashtable.values()
        