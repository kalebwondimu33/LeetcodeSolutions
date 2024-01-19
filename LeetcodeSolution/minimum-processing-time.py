class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        ans=[]
        k=3
        for i in range(len(processorTime)):
            ans.append(tasks[k]+processorTime[i])
            k+=4
        return max(ans)
            


