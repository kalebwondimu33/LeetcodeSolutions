class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        catch=[[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(word2)+1):
            catch[len(word1)][i]=len(word2)-i
        for j in range(len(word1)+1):
            catch[j][len(word2)]=len(word1)-j
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    catch[i][j]=catch[i+1][j+1]
                else:
                    catch[i][j]=1+min(catch[i][j+1],catch[i+1][j],catch[i+1][j+1])
        return catch[0][0]